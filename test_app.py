from app import simple_process

# Happy path
def test_simple_process():
    """simple_process logic = first * second + second"""
    first = 5
    second = 2
    assert simple_process(5, 2) == 12

# unhappy
def test_unhappy_simple_process():
    first = 5
    second = 2
    assert simple_process(5, 2, "negate") == 12