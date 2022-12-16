import flask
from server.game import FileTime, Savefile, Lexicon


class Pipeline:
    @classmethod
    def meta(cls, payload: dict):
        save = Savefile.read(flask.session["fn"])

        save.name.set(payload["name"])
        save.time.set(
            FileTime(
                ms=float(payload["ms"]),
                secs=float(payload["secs"]),
                mins=float(payload["mins"]),
                hours=float(payload["hours"])
            )
        )

        save.write()

    @classmethod
    def stats(cls, payload: dict):
        save = Savefile.read(flask.session["fn"])

        save.totalstrawberries.set(
            int(payload.pop("Reds")) + int(payload.pop("Goldens"))
        )

        for name, value in payload.items():
            save.get(name).set(int(value))

        save.write()

    @classmethod
    def mods(cls, payload: dict):
        save = Savefile.read(flask.session["fn"])
        print(payload)

        for name in ["AssistMode", "CheatMode", "VariantMode"]:
            save.get(name).set((payload.get(name) != None))

        if payload.get("AssistMode"):
            save.assists.dashmode.set(payload["DashMode"])
            save.assists.gamespeed.set(int(payload["GameSpeed"]))

        if payload.get("VariantMode"):
            for name in Lexicon.SEMANTICS["variants"]:
                save.get(name).set((payload.get(name) != None))

        save.write()

    @classmethod
    def flags(cls, payload: dict):
        save = Savefile.read(flask.session["fn"])
        save.theosistername.set(payload.pop("TheoSisterName"))

        for name in ["MetTheo", "TheoKnowsName"]:
            if payload.get(name) == "on" and name not in save.flags.value:
                save.flags.add(name)
            elif payload.get(name) == None and name in save.flags.value:
                save.flags.delete(name)

        save.write()
