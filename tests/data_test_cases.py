"""
Data for test case
"""

json_segment_i = """
{
    "state": {
        "seg": [
            {
                "id": 0,
                "i": [0, "FF00FF"]
            }
        ]
    }
}
"""

json_full_state = """
{
    "info": {
        "ver": "0.8.4",
        "vid": 1903252,
        "leds": {
            "count": 20,
            "rgbw": true,
            "pin": [
                2
            ],
            "pwr": 0,
            "maxpwr": 65000,
            "maxseg": 1
        },
        "name": "WLED Light",
        "udpport": 21324,
        "live": false,
        "fxcount": 80,
        "palcount": 47,
        "arch": "esp8266",
        "core": "2_4_2",
        "freeheap": 13264,
        "uptime": 17985,
        "opt": 127,
        "brand": "WLED",
        "product": "DIY light",
        "btype": "src",
        "mac": "60019423b441"
    },
    "effects": [
        "Solid",
        "Blink",
        "Breathe",
        "Wipe",
        "Wipe Random",
        "Random Colors",
        "Sweep",
        "Dynamic",
        "Colorloop",
        "Rainbow",
        "Scan",
        "Dual Scan",
        "Fade",
        "Chase",
        "Chase Rainbow",
        "Running",
        "Saw",
        "Twinkle",
        "Dissolve",
        "Dissolve Rnd",
        "Sparkle",
        "Dark Sparkle",
        "Sparkle+",
        "Strobe",
        "Strobe Rainbow",
        "Mega Strobe",
        "Blink Rainbow",
        "Android",
        "Chase",
        "Chase Random",
        "Chase Rainbow",
        "Chase Flash",
        "Chase Flash Rnd",
        "Rainbow Runner",
        "Colorful",
        "Traffic Light",
        "Sweep Random",
        "Running 2",
        "Red & Blue",
        "Stream",
        "Scanner",
        "Lighthouse",
        "Fireworks",
        "Rain",
        "Merry Christmas",
        "Fire Flicker",
        "Gradient",
        "Loading",
        "In Out",
        "In In",
        "Out Out",
        "Out In",
        "Circus",
        "Halloween",
        "Tri Chase",
        "Tri Wipe",
        "Tri Fade",
        "Lightning",
        "ICU",
        "Multi Comet",
        "Dual Scanner",
        "Stream 2",
        "Oscillate",
        "Pride 2015",
        "Juggle",
        "Palette",
        "Fire 2012",
        "Colorwaves",
        "BPM",
        "Fill Noise",
        "Noise 1",
        "Noise 2",
        "Noise 3",
        "Noise 4",
        "Colortwinkle",
        "Lake",
        "Meteor",
        "Smooth Meteor",
        "Railway",
        "Ripple"
    ],
    "palettes": [
        "Default",
        "Random Cycle",
        "Primary Color",
        "Based on Primary",
        "Set Colors",
        "Based on Set",
        "Party",
        "Cloud",
        "Lava",
        "Ocean",
        "Forest",
        "Rainbow",
        "Rainbow Bands",
        "Sunset",
        "Rivendell",
        "Breeze",
        "Red & Blue",
        "Yellowout",
        "Analogous",
        "Splash",
        "Pastel",
        "Sunset 2",
        "Beech",
        "Vintage",
        "Departure",
        "Landscape",
        "Beach",
        "Sherbet",
        "Hult",
        "Hult 64",
        "Drywet",
        "Jul",
        "Grintage",
        "Rewhi",
        "Tertiary",
        "Fire",
        "Icefire",
        "Cyane",
        "Light Pink",
        "Autumn",
        "Magenta",
        "Magred",
        "Yelmag",
        "Yelblu",
        "Orange & Teal",
        "Tiamat",
        "April Night"
    ],
    "state": {
        "off": true,
        "bri": 250,
        "transition": 7,
        "ps": -1,
        "pl": -1,
        "nl": {
            "on": false,
            "dur": 60,
            "mode": 1,
            "tbri": 0,
            "rem": -1
        },
        "udpn": {
            "send": false,
            "recv": false,
            "sgrp": 0,
            "rgrp": 0
        },
        "lor": 0,
        "mainseg": 0,
        "seg": [
            {
                "id": 0,
                "start": 0,
                "stop": 16,
                "len": 16,
                "grp": 1,
                "spc": 0,
                "of": 0,
                "on": true,
                "frz": false,
                "bri": 128,
                "cct": 127,
                "set": 0,
                "col": [
                    [
                        0,
                        0,
                        255
                    ],
                    [
                        0,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ],
                "fx": 15,
                "sx": 128,
                "ix": 128,
                "pal": 0,
                "c1": 128,
                "c2": 128,
                "c3": 16,
                "sel": true,
                "rev": false,
                "mi": false,
                "o1": false,
                "o2": false,
                "o3": false,
                "si": 0,
                "m12": 0
            }
        ]
    }
}
"""
