class Lexicon:
    # schema for translating XML elements to python dataclass
    TREE = (
        ("AssistMode",              {"type": "boolean"}),
        ("CheatMode",               {"type": "boolean"}),
        ("LastSave",                {"type": "text"}),
        ("Name",                    {"type": "text"}),
        ("TheoSisterName",          {"type": "text"}),
        ("Time",                    {"type": "filetime"}),
        ("TotalDashes",             {"type": "number", "min": 0, "max": None}),
        ("TotalDeaths",             {"type": "number", "min": 0, "max": None}),
        ("TotalGoldenStrawberries", {"type": "number", "min": 0, "max": 26}),
        ("TotalJumps",              {"type": "number", "min": 0, "max": None}),
        ("TotalStrawberries",       {"type": "number", "min": 0, "max": 176}),
        ("TotalWallJumps",          {"type": "number", "min": 0, "max": None}),
        ("UnlockedAreas",           {"type": "number", "min": 0, "max": 9}),
        ("VariantMode",             {"type": "boolean"}),
        ("Version",                 {"type": "text"}),
        ("RevealedChapter9",        {"type": "boolean"}),
        ("LastArea",                {"type": "shard"}),
        # -----
        ("SummitGems", {
            "type": "strlist",
            "count": 6,
            "justify": True,
            "struct": "boolean",
            "default": "false",
            "options": ("true", "false")
        }),
        ("Flags", {
            "type": "strlist",
            "count": 2,
            "justify": False,
            "struct": "string",
        }),
        ("Poem", {
            "type": "strlist",
            "count": 16,
            "justify": False,
            "struct": "string",
            "default": "",
            "options": (
                "fc", "fcr", "os", "osr",
                "cr", "crr", "cs", "csr",
                "t",  "tr",  "tf", "tfr",
                "ts", "tsr", "mc", "mcr"
            ),
        }),
        ("Assists", {
            "type": "nodelist",
            "children": (
                ("Assists/DashAssist",        {"type": "boolean"}),
                ("Assists/GameSpeed",         {"type": "number", "min": 0, "max": 160}),
                ("Assists/Hiccups",           {"type": "boolean"}),
                ("Assists/InfiniteStamina",   {"type": "boolean"}),
                ("Assists/Invincible",        {"type": "boolean"}),
                ("Assists/InvisibleMotion",   {"type": "boolean"}),
                ("Assists/LowFriction",       {"type": "boolean"}),
                ("Assists/MirrorMode",        {"type": "boolean"}),
                ("Assists/NoGrabbing",        {"type": "boolean"}),
                ("Assists/PlayAsBadeline",    {"type": "boolean"}),
                ("Assists/SuperDashing",      {"type": "boolean"}),
                ("Assists/ThreeSixtyDashing", {"type": "boolean"}),
                ("Assists/DashMode", {
                    "type": "select",
                    "options": ["Normal", "Two", "Infinite"],
                }),
            ),
        }),
    )

    SEMANTICS = {
        "chapters": {
            "00": ("Prologue",         None),
            "01": ("Forsaken City",    1),
            "02": ("Old Site",         2),
            "03": ("Celestial Resort", 3),
            "04": ("Golden Ridge",     4),
            "05": ("Mirror Temple",    5),
            "06": ("Reflection",       6),
            "07": ("Summit",           7),
            "08": ("Epilogue",         None),
            "09": ("Core",             8),
            "10": ("Farewell",         9)
        },
        "stats": (
            "TotalDeaths",
            "TotalDashes",
            "TotalJumps",
            "TotalWallJumps"
        ),
        "modes": (
          "AssistMode",
          "CheatMode",
          "VariantMode"
        ),
        "assists": {
            "number": ("GameSpeed", ),
            "select": ("DashMode", ),
            "toggle": (
              "Invincible",
              "DashAssist",
              "InfiniteStamina"
            )
        },
        "variants": (
          "MirrorMode",
          "ThreeSixtyDashing",
          "InvisibleMotion",
          "NoGrabbing",
          "LowFriction",
          "SuperDashing",
          "Hiccups",
          "PlayAsBadeline"
        )
    }
