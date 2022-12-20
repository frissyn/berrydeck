import copy
from .fields import *
from .areas import Areas
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

        setattr(self, "areas", Areas(self._tree))

        for name, attr in Lexicon.TREE:
            details = copy.deepcopy(attr)
            fn = details.pop("type")

            builder = {
                "text": TextField,
                "number": NumberField,
                "boolean": BooleanField,
                "select": SelectField,
                "nodelist": FieldList,
                "strlist": StructList,
                "filetime": FileTimeField
            }[fn]

            tail_name = name.split("/")[-1].lower()

            try: 
                field = builder(name, self, **details)
                setattr(self, tail_name, field)
            except AttributeError as e:
                setattr(self, tail_name, None)

    def write(self, path: str = None):
        path = self._path if not path else path

        self._tree.write(path)

        return True

    def get(self, name):
        attr = getattr(self, str(name).lower(), None)

        if not attr:
            return getattr(self.assists, str(name).lower(), None)

        return attr
