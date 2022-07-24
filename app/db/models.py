from os import path, scandir

from .. import env

if not env._Run.migrate is None:
    dir = path.join(env.BASE_DIR, env._Run.migrate)
    with scandir(dir) as it:
        for entry in it:
            if not entry.name.startswith('.py') and entry.is_file():
                file = entry.name[:entry.name.find('.')]
                __import__(f'{env._Run.migrate}.{file}')
