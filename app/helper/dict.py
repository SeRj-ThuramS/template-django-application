from base.type import Struct

def toStruct(_dict: dict):
    tmp = Struct()

    for key in _dict:
        setattr(tmp, key, _dict[key])

    return tmp
