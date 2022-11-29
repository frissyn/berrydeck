class Lexicon:
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
