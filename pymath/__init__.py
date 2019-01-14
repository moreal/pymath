from pymath.exceptions import NotFunctionOperationException


class Function:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise NotFunctionOperationException()

        def new_function(*args, **kwargs):
            return self.function(*args, **kwargs) + other.function(*args, **kwargs)

        return Function(new_function)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise NotFunctionOperationException()

        def new_function(*args, **kwargs):
            return self.function(other.function(*args, **kwargs))

        return Function(new_function)
