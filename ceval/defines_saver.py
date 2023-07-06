import dataclasses
import errors

@dataclasses.dataclass
class Macro:
    """this is a simple data class that uses the
    name and the value of a specific macro to save it."""
    name: str
    value: str


def check_type(type_):
    def check_type_(function):
        def new_func(self, value):
            if isinstance(value, Macro):
                raise TypeError(str(type_)+" does not "+str(type_)+" object.")
            new_func.__doc__ = function.__doc__
            return function(value)
        return new_func
    check_type.__doc__ = check_type_.__doc__
    return check_type_


class MacroSaver:

    __Macros: list = []

    @check_type(Macro)
    def check_unique(self, macro: Macro):

        for m in self.__Macros:
            if macro.name == m.name:
                raise errors.UniqueNameError(macro.name, m.name)

    @check_type(Macro)
    def __add__(self, macro: Macro):
        self.__Macros.append(macro)

    @check_type(str)
    def __sub__(self, name: str):
        pass














