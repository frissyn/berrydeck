from .filetime import FileTime
import xml.etree.ElementTree as ET


class Field():
    def __init__(self, name: str, save):
        self.name = name
        self.tree = save._tree
        self.node = save._tree.find(name)
        self.value = self.node.text

    def __call__(self, *args, **kwargs):
        # so scuffed, so cursed. lord have mercy
        if args or kwargs:
            return self.__init__(*args, **kwargs)

        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def set(self, value):
        self.value = value
        self.node.text = str(value)

        return value


class TextField(Field):
    pass


class NumberField(Field):
    def __init__(self, name: str, save, **extras):
        super().__init__(name, save)
        self.value = int(self.value)
        self.min, self.max = extras["min"], extras["max"]

    def set(self, value):
        n = int(value)
        super().set(value)

        if self.max:
            max(self.min, min(n, self.max))

        self.value = int(self.value)
        self.node.text = str(value)

        return int(value)

    def add(self, n):
        self.set(self.value + n)


class BooleanField(Field):
    def __init__(self, name: str, save):
        super().__init__(name, save)

        self.value = True if self.value == "true" else False
    
    def set(self, value):
        super().set(value)
        self.node.text = str(value).lower()


    def toggle(self):
        if not self.value:
            self.set(True)
        else:
            self.set(False)


class SelectField(Field):
    def __init__(self, name: str, save, **extras):
        super().__init__(name, save)
        self.options = extras["options"]

    def set(self, value):
        if value not in self.options:
            raise ValueError(f'"{value}" is not a valid option for tag <{self.name}>')
        else:
            super().set(value)


class FileTimeField(Field):
    def __init__(self, name: str, save, **extras):
        super().__init__(name, save)

        self.value = FileTime(int(self.value))

    def set(self, value):
        self.value = value
        self.node.text = str(value.units)

        return value


class FieldList(list):
    def __init__(self, name: str, save, **extras):
        self.name = name
        self.children = []
        self.tree = save._tree

        for n, attr in extras["children"]:
            typ = attr.pop("type")

            if typ == "text":
                f = TextField(n, save)
            elif typ == "number":
                f = NumberField(n, save, **attr)
            elif typ == "boolean":
                f = BooleanField(n, save)
            elif typ == "select":
                f = SelectField(n, save, options=attr["options"])

            self.children.append(f)
            setattr(self, n.split("/")[-1].lower(), f)

        super().__init__(self.children)


class StructList(Field):
    def __init__(self, name: str, save, **extras):
        super().__init__(name, save)
        self.max = extras["count"]
        self.struct = extras["struct"]
        self.justify = extras["justify"]
        self.options = extras.get("options", [])
        self.default = extras.get("default", "")
        self.value = list(map(lambda x: x.text, self.node))

    def __getitem__(self, *args, **kwargs):
        return self.value.__getitem__(*args, **kwargs)

    def add(self, value):
        el = ET.Element(self.struct)
        el.text = value

        self.node.append(el)
        self.value = list(map(lambda x: x.text, self.node))

    def set(self, index: int, value):
        self.value[index] = value
        self.node[index].text = value

    def delete(self, name: str):
        index = self.value.index(name)
        print(index, name)
        print(list(self.node), list(self.node)[index])

        self.node.remove(list(self.node)[index])
        del self.value[index]

    def set_as(self, values):
        self.node.clear()

        if self.justify:
            values += [self.default, ] * (self.max - len(values))

        for value in values:
            if value not in self.options and self.default != "":
                raise ValueError(f"'{value}' is not a valid value for <{self.name}>.")

            el = ET.Element(self.struct)
            el.text = value

            self.node.append(el)

        self.value = list(map(lambda x: x.text, self.node))
