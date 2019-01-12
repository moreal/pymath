class NotFunctionOpertiaonException(Exception):
    pass

class Function:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

    def __add__(self, other: Function):
        if not isinstance(other, Function):
            raise NotFunctionOpertiaonException()

        def new_function(x):
            return self.function(x) + other.function(x)

        return Function(new_function)

    def __mul__(self, other: Function):
        if not isinstance(other, Function):
            raise NotFunctionOpertiaonException()

        def new_function(x):
            return self.function(other.function(x))

        return Function(new_function)
