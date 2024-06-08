from colour import Color

from wled_adapter.segment import Segment


def test_get_optimised_colour_changes_single_color():
    """
    Test case for the `get_optimised_colour_changes` method when the segment has a
    single color.

    It sets all LEDs in the segment to a specified color and checks if the optimized
    color changes are correctly returned.

    Returns:
        None
    """
    segment = Segment(5)
    color = Color("red")
    segment.set_all(color)
    assert segment.get_optimised_colour_changes() == [0, 4, color]


def test_get_optimised_colour_changes_multiple_colors():
    """
    Test case for the `get_optimised_colour_changes` method when the segment has
    multiple colors.

    It sets different color ranges in the segment and checks if the optimized color
    changes are correctly returned.

    Returns:
        None
    """
    segment = Segment(10)
    segment.set_range(0, 4, Color("red"))
    segment.set_range(5, 9, Color("blue"))
    assert segment.get_optimised_colour_changes() == [
        0,
        4,
        Color("red"),
        5,
        9,
        Color("blue"),
    ]


def test_get_optimised_colour_changes_alternated_colors():
    """
    Test case for the `get_optimised_colour_changes` method when the segment has
    alternated colors.

    It sets alternating colors in the segment and checks if the optimized color changes
    are correctly returned.

    Returns:
        None
    """
    segment = Segment(10)
    for i in range(len(segment)):
        segment[i] = Color("red") if i % 2 == 0 else Color("blue")
    assert segment.get_optimised_colour_changes() == [
        0,
        Color("red"),
        Color("blue"),
        Color("red"),
        Color("blue"),
        Color("red"),
        Color("blue"),
        Color("red"),
        Color("blue"),
        Color("red"),
        Color("blue"),
    ]


def test_get_optimised_colour_changes_no_changes():
    """
    Test case for the `get_optimised_colour_changes` method when the segment has no
    color changes.

    It checks if an empty list is returned when there are no color changes in the
    segment.

    Returns:
        None
    """
    segment = Segment(8)
    segment.reset_changes()
    assert segment.get_optimised_colour_changes() == []


def test_get_optimised_colour_changes_empty_segment():
    """
    Test case for the `get_optimised_colour_changes` method when the segment is empty.

    It checks if an empty list is returned when the segment has no LEDs.

    Returns:
        None
    """
    segment = Segment(0)
    assert segment.get_optimised_colour_changes() == []
