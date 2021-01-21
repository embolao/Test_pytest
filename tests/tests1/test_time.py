import pytest

from datetime import datetime, timedelta

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]


@pytest.mark.parametrize("a, b, expected", testdata)
def test_timedistance_v0(a, b, expected):
    """docstring for test_timedistance_v0"""
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a, b, expected", testdata, ids=["forwar", "backward"])
def test_timedistance_v1(a, b, expected):
    """docstring for test_timedistance_v1"""
    diff = a - b
    assert diff == expected


def idfn(val):
    """docstring for idfn"""
    if isinstance(val, (datetime,)):
        return val.strftime("%Y%m%d")


@pytest.mark.parametrize("a, b, expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    """docstring for test_timedistance_v2"""
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(
            datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1), id="forward"
        ),
        pytest.param(
            datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1), id="backward"
        ),
    ],
)
def test_timedistance_v3(a, b, expected):
    """docstring for test_timedistance_v3"""
    diff = a - b
    assert diff == expected
