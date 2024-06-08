from wled_adapter.state import Info, Leds, Nl, Seg, State, Udpn, WledData

from .data_test_cases import json_full_state


def test_sample_status_message_deserialization():
    state = WledData.from_json(json_full_state)
    assert state.info.leds.count == 20
    assert state.effects[0] == "Solid"
    assert state.effects[-1] == "Ripple"
    assert state.palettes[0] == "Default"
    assert state.palettes[-1] == "April Night"
    assert state.state.seg[0].len == 16


def test_json_serialization():
    # Create an instance of each data class
    leds = Leds(count=10, rgbw=True, pin=[1, 2, 3], pwr=100, maxpwr=200, maxseg=5)
    info = Info(ver="1.0.0", vid=123, leds=leds, name="WLED Device", udpport=8888)
    nl = Nl(on=True, dur=60, mode=1, tbri=128, rem=30)
    udpn = Udpn(send=True, recv=True, sgrp=1, rgrp=2)
    seg = Seg(
        id=1,
        start=0,
        stop=9,
        len=10,
        grp=1,
        spc=1,
        of=0,
        on=True,
        bri=255,
        cct=0,
        set=0,
        col=[[255, 0, 0]],
        fx=0,
        sx=0,
        ix=0,
        pal=0,
        c1=0,
        c2=0,
        c3=0,
        sel=True,
        rev=False,
        mi=False,
        o1=False,
        o2=False,
        o3=False,
        si=0,
        m12=0,
        i=[0, "string"],
    )
    state = State(
        off=False,
        bri=128,
        transition=1000,
        ps=0,
        pl=0,
        nl=nl,
        udpn=udpn,
        lor=0,
        mainseg=1,
        seg=[seg],
    )
    wled_data = WledData(
        info=info,
        effects=["effect1", "effect2"],
        palettes=["palette1", "palette2"],
        state=state,
    )

    # Serialize the data class instance to JSON
    json_data = wled_data.to_json()

    # Deserialize the JSON back to data class instance
    deserialized_data = WledData.from_json(json_data)

    # Assert that the deserialized data is equal to the original data
    assert deserialized_data == wled_data


def test_json_deserialization():
    # Create a JSON string representing an instance of WledData
    json_data = """
    {
        "info": {
            "ver": "1.0.0",
            "vid": 123,
            "leds": {
                "count": 10,
                "rgbw": true,
                "pin": [1, 2, 3],
                "pwr": 100,
                "maxpwr": 200,
                "maxseg": 5
            },
            "name": "WLED Device",
            "udpport": 8888
        },
        "effects": ["effect1", "effect2"],
        "palettes": ["palette1", "palette2"],
        "state": {
            "off": false,
            "bri": 128,
            "transition": 1000,
            "ps": 0,
            "pl": 0,
            "nl": {
                "on": true,
                "dur": 60,
                "mode": 1,
                "tbri": 128,
                "rem": 30
            },
            "udpn": {
                "send": true,
                "recv": true,
                "sgrp": 1,
                "rgrp": 2
            },
            "lor": 0,
            "mainseg": 1,
            "seg": [
                {
                    "id": 1,
                    "start": 0,
                    "stop": 9,
                    "len": 10,
                    "grp": 1,
                    "spc": 1,
                    "of": 0,
                    "on": true,
                    "bri": 255,
                    "cct": 0,
                    "set": 0,
                    "col": [[255, 0, 0]],
                    "fx": 0,
                    "sx": 0,
                    "ix": 0,
                    "pal": 0,
                    "c1": 0,
                    "c2": 0,
                    "c3": 0,
                    "sel": true,
                    "rev": false,
                    "mi": false,
                    "o1": false,
                    "o2": false,
                    "o3": false,
                    "si": 0,
                    "m12": 0,
                    "i": [0, "string"]
                }
            ]
        }
    }
    """

    # Deserialize the JSON string to a data class instance
    deserialized_data = WledData.from_json(json_data)

    # Create an instance of each data class manually
    leds = Leds(count=10, rgbw=True, pin=[1, 2, 3], pwr=100, maxpwr=200, maxseg=5)
    info = Info(ver="1.0.0", vid=123, leds=leds, name="WLED Device", udpport=8888)
    nl = Nl(on=True, dur=60, mode=1, tbri=128, rem=30)
    udpn = Udpn(send=True, recv=True, sgrp=1, rgrp=2)
    seg = Seg(
        id=1,
        start=0,
        stop=9,
        len=10,
        grp=1,
        spc=1,
        of=0,
        on=True,
        bri=255,
        cct=0,
        set=0,
        col=[[255, 0, 0]],
        fx=0,
        sx=0,
        ix=0,
        pal=0,
        c1=0,
        c2=0,
        c3=0,
        sel=True,
        rev=False,
        mi=False,
        o1=False,
        o2=False,
        o3=False,
        si=0,
        m12=0,
        i=[0, "string"],
    )
    state = State(
        off=False,
        bri=128,
        transition=1000,
        ps=0,
        pl=0,
        nl=nl,
        udpn=udpn,
        lor=0,
        mainseg=1,
        seg=[seg],
    )
    expected_data = WledData(
        info=info,
        effects=["effect1", "effect2"],
        palettes=["palette1", "palette2"],
        state=state,
    )

    # Assert that the deserialized data is equal to the manually created instance
    assert deserialized_data == expected_data
