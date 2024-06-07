import pytest
from wled_adapter.state import WledData
from .data_test_cases import * 

def test_deserialization():
    test_object = WledData.from_json(json_full_state)
    pass

def test_seg_i_1():
    test_object = WledData.from_json(json_segment_i)
    pass