from .locale import _dict
from . import env
from . import app

lng = _dict[env._Run.locale]

def Init(argv = None):
    if argv is None:
        print(lng['tda_argv_none'])

        exit()

    if not isinstance(argv, list):
        print(lng['tda_argv_type_error'])

        exit()

    param = None

    for arg in argv:
        if arg[0:2] == '--':
            param = arg[2:]
            if param == 'debug':
                env._Run.debug = True
                env._Run.release = False

            continue

        elif param == 'name':
            env._Run.name = arg
        elif param == 'migrate':
            env._Run.migrate = arg
        else:
            env._Run.app.append( (param, arg) )


    if env._Run.name is None:
        print(lng['tda_argv_name_none'])

        exit()

    app.Run()
