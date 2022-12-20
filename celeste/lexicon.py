class Lexicon:
    # Schema for translating <AreaModeStats /> attrs to Python attributes.
    ATTRIB = (
        ("BestDashes", {
            "type": "number",
            "min": 0, "max": None,
            "tip": "Least number of dashes used in a full clear of this level."
        }),
        ("BestDeaths", {
            "type": "number",
            "min": 0, "max": None,
            "tip": "Least number of deaths in a full clear of this level."
        }),
        ("BestFullClearTime", {
            "type": "filetime",
            "tip": "Shortest elasped time for a full clear of this level."
        }),
        ("BestTime", {
            "type": "filetime",
            "tip": "Shortest elaspsed time for all checkpoints of this level."
        }),
        ("Completed", {
            "type": "boolean",
            "tip": "Comepletion status of this level."
        }),
        ("Deaths", {
            "type": "number",
            "min": 0, "max": None,
            "tip": "Total number of deaths for this level."
        }),
        ("FullClear", {
            "type": "boolean",
            "tip": "Full clear completetion status for this level. Requires all"
                   "entities to be collected in a single session."
        }),
        ("HeartGem", {
            "type": "boolean",
            "tip": "Collection status for this level's heart."
        }),
        ("SingleRunCompleted", {
            
        }),
        ("TimePlayed", {
            "type": "filetime",
            "tip": "Total elapsed time spent playing this level."
        }),
        ("TotalStrawberries", {
            "type": "number",
            "min": 0, "max": None,
            "tip": "Total number of strawberries collected in this level."
        }),
    )

    # Schema for translating root-level XML elements to Python "Savefile(...)"
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
        # ("LastArea",                {"type": "text"}),
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
        "assists": {
            "number": ("GameSpeed", ),
            "select": ("DashMode", ),
            "toggle": (
              "Invincible",
              "DashAssist",
              "InfiniteStamina"
            )
        },
        "chapters": {
            "00": ("Prologue",         None, {"A": True, "B": None, "C": None}),
            "01": ("Forsaken City",    1,    {"A": True, "B": True, "C": True}),
            "02": ("Old Site",         2,    {"A": True, "B": True, "C": True}),
            "03": ("Celestial Resort", 3,    {"A": True, "B": True, "C": True}),
            "04": ("Golden Ridge",     4,    {"A": True, "B": True, "C": True}),
            "05": ("Mirror Temple",    5,    {"A": True, "B": True, "C": True}),
            "06": ("Reflection",       6,    {"A": True, "B": True, "C": True}),
            "07": ("Summit",           7,    {"A": True, "B": True, "C": True}),
            "08": ("Epilogue",         None, {"A": True, "B": None, "C": None}),
            "09": ("Core",             8,    {"A": True, "B": True, "C": True}),
            "10": ("Farewell",         9,    {"A": True, "B": None, "C": None})
        },
        "modes": ("AssistMode", "CheatMode", "VariantMode"),
        "stats": ("TotalDeaths", "TotalDashes", "TotalJumps", "TotalWallJumps"),
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
