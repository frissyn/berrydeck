import copy
from .filetime import FileTime
import xml.etree.ElementTree as ET 


class Areas():
    def __init__(self, root: ET.ElementTree):
        self._tree = root
        self._items = list(map(Area, root.find("Areas")))

    def __iter__(self, *args, **kwargs):
        return self._items.__iter__(*args, **kwargs)

    def __next__(self, *args, **kwargs):
        return self._items.__next__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        return self._items.__getitem__(*args, **kwargs)


class Area():
    def __init__(self, el: ET.Element):
        self.attributes = copy.deepcopy(el.attrib)

        for name, value in el.attrib.items():
            setattr(self, name, value)

        # lists!!!!! (kill me)
        setattr(self, "modes", list(map(Mode, list(list(el)[0]))))

    def __iter__(self, *args, **kwargs):
        return self.modes.__iter__(*args, **kwargs)

    def __next__(self, *args, **kwargs):
        return self.modes.__next__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        if isinstance(args[0], str):
            # quite clever, if u ask me
            return self.modes.__getitem__(["A", "B", "C"].index(args[0]))

        return self.modes.__getitem__(*args, **kwargs)


class Mode():
    def __init__(self, el: ET.Element):
        self.attributes = copy.deepcopy(el.attrib)

        for name, value in el.attrib.items():
            setattr(self, name.lower(), value)

    def get(self, name):
        return getattr(self, str(name).lower(), None)
