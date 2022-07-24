from .type import Struct
from .locale import default as LNG

_Run = Struct()

_Run.name = None
_Run.app = []
_Run.pool = []
_Run.models = None
_Run.migrate = None
_Run.release = True
_Run.debug = False
_Run.locale = LNG

BASE_DIR = None
log = None
reload = False
