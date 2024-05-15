from firstpython import more_hello, more_goodbye


def test_more_hello():
    assert "New python file" == more_hello()


def test_more_goodbye():
    assert "New bye" == more_goodbye()
