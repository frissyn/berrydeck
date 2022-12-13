import re
import datetime as dt


class FileTime(object):
    def __init__(self, units: int = 1, **clock):
        if clock:
            units = sum([
                clock.get("ms",    0),
                clock.get("secs",  0) * 1000.0,
                clock.get("mins",  0) * 60000.0,
                clock.get("hours", 0) * 3600000.0,
                clock.get("days",  0) * 86400000.0,
            ]) * 10000.0

        self.units = int(units)
        self.delta = dt.timedelta(milliseconds=(units / 10000.0))

        self.ms    = self.delta.total_seconds() * 1000.0
        self.secs  = float(self.delta.total_seconds())
        self.mins  = self.delta.total_seconds() / 60.0
        self.hours = self.delta.total_seconds() / 3600.0
        self.days  = self.delta.total_seconds() / 86400.0


    def __str__(self):
        return self.fclock()

    def __repr__(self):
        return self.fclock()

    def __add__(self, b):
        return FileTime(self.units + b.units)

    def __sub__(self, b):
        return FileTime(self.units - b.units)

    @classmethod
    def make(cls, days=0, hours=0, mins=0, secs=0, ms=0):
        return cls(
            sum([
                days * 86400000.0,
                hours * 3600000.0,
                mins * 60000.0,
                secs * 1000.0,
                ms
            ]) * 10000.0
        )

    def fclock(self):
        ms = self.delta.total_seconds() * 1000.0
    
        hrs, remain = divmod(ms, 3600000)
        min, remain = divmod(remain, 60000)
        sec, ms = divmod(remain, 1000)
        ms = round(ms)
    
        return ":".join([
            f"{int(hrs)}".zfill(2),
            f"{int(min)}".zfill(2),
            f"{int(sec)}".zfill(2),
        ]) + (f".{str(ms).split('.')[0]}" if ms != 0 else ".000")

    def iclock(self):
        nums = re.split("\:|\.", self.fclock())

        return [
            int(nums[0]),
            int(nums[1]),
            int(nums[2]),
            float(nums[3])
        ]
