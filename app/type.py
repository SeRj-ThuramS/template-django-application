class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class srcRunStruct:
    src = None
    config = []
