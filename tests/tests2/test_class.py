class TestClass:
    """description"""
    def test_one(self):
        """docstring for test_one"""
        x = "this"
        assert "h" in x

    def test_two(self):
        """docstring for test_two"""
        x = "hello"
        assert hasattr(x, "check")
