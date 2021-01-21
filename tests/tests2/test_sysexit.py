import pytest


def f():
    """docstring for f"""
    raise SystemExit(1)


def test_mytest():
    """docstring for test_mytest"""
    with pytest.raises(SystemExit):
        f()
