from src.main import function


def test_function_returns_string():
    expected = "Hello World"

    actual = function()

    assert actual == expected
