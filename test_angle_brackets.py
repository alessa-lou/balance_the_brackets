import pytest
from angle_brackets import Angles

def test_check():
    angles = Angles()
    assert angles.check("<<><><") == "<<><><>>"
    assert angles.check("><><><") == "<><><><>"
    assert angles.check(">>><>") == "<>>><>"
    assert angles.check("><><><<") == "<><><><<>>"
    assert angles.check("<><><><<<<") == "<><><><<<<>>>>"

