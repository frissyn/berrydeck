from .fields import *
from .lexicon import Lexicon
import xml.etree.ElementTree as ET

class Savefile(object):
    def __init__(self, data: str, path: str = None):
        self._raw, self._path = data, path
        self._tree = ET.ElementTree(ET.fromstring(data))

        # attach xpath elements to savefile class.
        # so SaveData/Assists/DashMode, for example,
        # becomes savefile.assists.dashmode
        self._propogate_handles()

    @classmethod
    def read(cls, path: str):
        with open(path, "r+") as fh:
            raw = str(fh.read())

        return cls(raw, path)

    def _propogate_handles(self):
        builder = NotImplemented

        for name, attr in Lexicon.TREE:
            attr = attr.copy()
            fn = attr.pop("type")

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
                continue
            # else: 
            #     continue

            tail_name = name.split("/")[-1].lower()

            field = builder(name, self, **attr)
            setattr(self, tail_name, field)
