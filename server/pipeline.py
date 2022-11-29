import flask
from server.game import FileTime, Savefile


class Pipeline:
    @classmethod
    def meta(cls, values: dict):
        payload = {
            "Name": values["name"],
            "Time": FileTime.make(
                hours=float(values["hours"]),
                mins=float(values["mins"]),
                secs=float(values["secs"]),
                ms=float(values["ms"])
            ).units
        }

        sf = Savefile(flask.session["fn"])
        sf.push(payload)

    @classmethod
    def stats(cls, values: dict):
        values.pop("rs")
        
        payload = {
            "TotalStrawberries": values.pop("ts"),
            "TotalGoldenStrawberries": values.pop("gs"),
            **values
        }

        sf = Savefile(flask.session["fn"])
        sf.push(payload)

    @classmethod
    def mods(cls, values: dict):
        print(values)
