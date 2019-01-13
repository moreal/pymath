import init_path

from pymath import Function
from pymath import decorators


def test_function_decorator():

    @decorators.func
    def some_function():
        return 1

    assert isinstance(some_function, Function)


def test_function_call():

    @decorators.func
    def some_function():
        return 1

    assert 1 == some_function()

def test_function_add():
    @decorators.func
    def a():
        return 1

    @decorators.func
    def b():
        return 2

    new_function = a + b

    assert 3 == new_function()

def test_function_mul():
    @decorators.func
    def a(x):
        return x + 1

    @decorators.func
    def b(x):
        return x + 2

    new_function = a*b

    assert 4 == new_function(1)
