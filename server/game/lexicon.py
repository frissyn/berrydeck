class Lexicon:
    # tuples > lists
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
            "struct": "boolean",
            "options": ("true", "false"),
        }),
        ("Flags", {
            "type": "strlist",
            "count": 16,
            "struct": "string",
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
                ("Assists/DashMode", {
                    "type": "select",
                    "options": ["Normal", "Two", "Infinite"],
                }),
                ("Assists/GameSpeed",         {"type": "number", "min": 0, "max": 160}),
                ("Assists/Hiccups",           {"type": "boolean"}),
                ("Assists/InfiniteStamina",   {"type": "boolean"}),
                ("Assists/Invincible",        {"type": "boolean"}),
                ("Assists/InvisibleMotion",   {"type": "boolean"}),
                ("Assists/LowFriction",       {"type": "boolean"}),
                ("Assists/MirrorMode",        {"type": "boolean"}),
                ("Assists/NoGrabbing",        {"type": "boolean"}),
                ("Assists/PlayAsBadeline",     {"type": "boolean"}),
                ("Assists/SuperDashing",      {"type": "boolean"}),
                ("Assists/ThreeSixtyDashing", {"type": "boolean"}),
            ),
        })
    )

    ATTRS = {
        "type:text": (
            "Name",
            "Version",
            "LastSave",
            "TheoSisterName"
        ),
        "type:boolean": (
            "AssistMode",
            "CheatMode",
            "VariantMode"
        ),
        "type:number": (
            ("TotalDashes",             {"min": 0, "max": None}),
            ("TotalDeaths",             {"min": 0, "max": None}),
            ("TotalGoldenStrawberries", {"min": 0, "max": 26}),
            ("TotalJumps",              {"min": 0, "max": None}),
            ("TotalStrawberries",       {"min": 0, "max": 176}),
            ("TotalWallJumps",          {"min": 0, "max": None}),
            ("UnlockedAreas",           {"min": 1, "max": 10})
        ),
        "type:select": (
            ("Assists/DashMode",        ["Normal", "Two", "Infinite"]),
        )
    }

    STATS = {
        "normal": [
            'TotalDeaths',
            'TotalJumps',
            'TotalWallJumps',
            'TotalDashes'
        ]
    }
    MODES = ['AssistMode', 'CheatMode', 'VariantMode']
    ASSISTS = {
        "number": ["Assists/GameSpeed"],
        "select": ["Assists/DashMode"],
        "toggle": [
          "Assists/Invincible",
          "Assists/DashAssist",
          "Assists/InfiniteStamina"
        ]
    }
    VARIANTS = [
        "Assists/MirrorMode",
        "Assists/ThreeSixtyDashing",
        "Assists/InvisibleMotion",
        "Assists/NoGrabbing",
        "Assists/LowFriction",
        "Assists/SuperDashing",
        "Assists/Hiccups",
        "Assists/PlayAsBadeline"
    ]
