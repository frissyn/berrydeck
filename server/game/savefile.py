import copy
from .fields import *
from .lexicon import Lexicon
import xml.etree.ElementTree as ET


class Savefile(object):
    def __init__(self, data: [str, bytes], path: str = None):
        self._raw, self._path = data, path
        self._tree = ET.ElementTree(ET.fromstring(data))

        # attach xpath elements to savefile class
        # as properties. so SaveData/Assists/DashMode,
        # for example, becomes savefile.assists.dashmode
        self._propogate_handles()

    @classmethod
    def read(cls, path: str):
        with open(path, "r+") as fh:
            raw = str(fh.read())

        return cls(raw, path)

    def _propogate_handles(self):
        builder = NotImplemented

        for name, attr in Lexicon.TREE:
            details = copy.deepcopy(attr)
            fn = details.pop("type")

            if fn == "text":
                builder = TextField
            elif fn == "number":
                builder = NumberField
            elif fn == "boolean":
                builder = BooleanField
            elif fn == "select":
                builder = SelectField
            elif fn == "nodelist":
                builder = FieldList
            elif fn == "strlist":
                builder = StructList
            elif fn == "filetime":
                builder = FileTimeField

            tail_name = name.split("/")[-1].lower()

            field = builder(name, self, **details)
            setattr(self, tail_name, field)

    def write(self, path: str = None):
        path = self._path if not path else path

        self._tree.write(path)

        return True

    def get(self, name):
        attr = getattr(self, str(name).lower(), None)

        if not attr:
            return getattr(self.assists, str(name).lower())

        return attr
