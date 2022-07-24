import time
import multiprocessing
import threading
import traceback

from . import env
from . import locale as LNG

def Create(q):
    import os
    import traceback
    from transliterate import slugify

    from . import env
    from .locale import _dict, default
    from .settings import TIME_ZONE
    from app.helper import logger

    env.BASE_DIR, env._Run.name, env._Run.app, env._Run.models, \
                    env._Run.migrate, env._Run.release, \
                    env._Run.debug, env._Run.locale = q.get()

    lng = _dict[ default ]

    if hasattr(time, 'tzset'):
        os.environ['TZ'] = TIME_ZONE
        time.tzset()

    try:
        env.log = logger.Start(slugify(f'апп_{env._Run.name}'))
    except Exception as e:
        print( lng["tda_error_create_logging"].format(traceback.format_exc()) )
        return

    env.log.info(lng["tda_01_basic"])

    # Django specific settings
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
        env.log.debug(lng["tda_02_default_django"])
    except Exception:
        env.log.critical( lng["tda_02_default_django_error"].format(traceback.format_exc()) )
        return

    try:
        import django
        django.setup()
        env.log.info( lng['tda_04_completed'] )
    except Exception:
        env.log.critical( lng['tda_04_completed_error'].format(traceback.format_exc()) )
        return

    if not env._Run.migrate is None:
        env.log.info( lng["tda_03_migrate_db"] )
        try:
            from django.core import management
            management.call_command("makemigrations", "db")
            env.log.debug( lng["tda_03_migrate_db_prepare"] )
        except Exception as e:
            env.log.critical( lng["tda_03_migrate_db_prepare_error"].format(traceback.format_exc()))
            return

        try:
            management.call_command("migrate")
            env.log.debug( lng["tda_03_migrate_db_pull"] )
        except Exception as e:
            env.log.critical( lng["tda_03_migrate_db_pull_error"].format(traceback.format_exc()))
            return
    else:
        env.log.warning( lng['tda_03_migrate_db_disable'] )

    for app in env._Run.app:
        try:
            env.log.info( lng['tda_05_module'].format(app[0]) )
            __import__(f'{app[0]}.{app[1]}')
        except Exception as e:
            env.log.critical( lng["tda_05_module_error"].format(f'{app[0]}.{app[1]}', traceback.format_exc()))
            return

def prAwait():
    from .locale import _dict, default
    lng = _dict[ default ]

    while True:
        if env.reload:
            try:
                print( lng['tda_debug_restart'].format(env._Run.name) )

                pr = [obj for obj in env._Run.pool if obj.name == 'app'][0]
                pr.kill()

                while True:
                    if not pr.is_alive():
                        env._Run.pool.remove(pr)
                        env.reload = False

                        break

                q = multiprocessing.Queue()

                res = (env.BASE_DIR, env._Run.name, env._Run.app, env._Run.models, env._Run.migrate,
                        env._Run.release, env._Run.debug, env._Run.locale)
                q.put( res )
                p = multiprocessing.Process(target=Create, args=(q, ), daemon=True, name='app')
                env._Run.pool.append(p)

                p.start()
            except Exception as e:
                print( lng['tda_debug_restart'].format(env._Run.name, traceback.format_exc()) )
                exit()

        time.sleep(1)

def on_modified(event):
    env.reload = True

def Run():
    from .locale import _dict, default
    lng = _dict[ default ]

    proccess_current = multiprocessing.current_process()
    proccess_current.name = 'main'
    env._Run.pool.append(proccess_current)

    q = multiprocessing.Queue()

    res = (env.BASE_DIR, env._Run.name, env._Run.app, env._Run.models, env._Run.migrate,
            env._Run.release, env._Run.debug, env._Run.locale)
    q.put( res )
    p = multiprocessing.Process(target=Create, args=(q, ), daemon=True, name='app')
    env._Run.pool.append(p)

    if env._Run.release:
        p.start()
    elif env._Run.debug:
        from .settings import ignore_directories, case_sensitive, \
                            ignore_patterns, patterns

        try:
            from watchdog.observers import Observer
            from watchdog.events import PatternMatchingEventHandler
        except ImportError:
            print( lng['tda_error_watchdog'] )
            exit()

        try:
            threading.Thread(target=prAwait, args=(), daemon=True, name='prAwait').start()

            my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns,
                                                            ignore_directories, case_sensitive)

            my_event_handler.on_modified = on_modified

            my_observer = Observer()
            my_observer.schedule(my_event_handler, env.BASE_DIR, recursive=True)
            my_observer.start()

            p.start()
        except Exception as e:
            print( lng['tda_error_debug_func'].format(traceback.format_exc()) )

    try:
        while True:
            if env._Run.release:
                if not p.is_alive():
                    break
            elif env._Run.debug:
                pass

            time.sleep(0.1)
        exit()
    except KeyboardInterrupt:
        if env._Run.release:
            p.kill()
        elif env._Run.debug:
            pass
            # exit()

        # proccess_current.terminate()
