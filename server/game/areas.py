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
        for name, value in el.attrib.items():
            setattr(self, name, value)

