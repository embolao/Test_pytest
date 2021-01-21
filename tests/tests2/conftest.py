def pytest_addoption(parser):
    """docstring for pytest_addoption"""
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="List of stringinput to pass to test functions"
    )


def pytest_generate_tests(metafunc):
    """docstring for pytest_generate_tests"""
    metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
