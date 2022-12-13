from .filetime import FileTime


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
        self.tree.find(self.name).text = value

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

        max(self.min, min(n, self.max))
        self.value = int(self.value)

        return int(value)

    def add(self, n):
        self.set(self.value + n)


class BooleanField(Field):
    def toggle(self):
        if self.value == "true":
            self.set("false")
        elif self.value == "false":
            self.set("true")


class SelectField(Field):
    def __init__(self, name: str, save, **extras):
        super().__init__(name, save)
        self.options = extras["options"]

    def set(self, value):
        if value not in self.options:
            raise TypeError(f'"{value}" is not a valid option for tag <{self.name}>')
        else:
            super().set(value)


class FileTimeField(Field):
    def __init__(self, name: str, save, **extras):
        super().__init__(name, save)

        self.value = FileTime(int(self.value))


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


class StructList(list):
    def __init__(self, *args, **kwargs):
        pass
