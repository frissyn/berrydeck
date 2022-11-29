import xml.etree.ElementTree as ET


class Savefile(object):
    def __init__(self, path: str):
        self.path = path

        with open(path, "r") as fh:
            self.data = ET.fromstring(str(fh.read()))
            self.data = ET.ElementTree(self.data)

    def push(self, payload: dict):
        for name, values in payload.items():
            self.data.find(name).text = str(values)

        result = ET.tostring(self.data.getroot())

        with open(self.path, "w+") as fh:
            fh.write(result.decode('UTF-8'))
