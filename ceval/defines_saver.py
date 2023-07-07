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
        def new_func(value):
            if isinstance(value, Macro):
                raise TypeError(str(type_)+" does not "+str(type_)+" object.")
            new_func.__doc__ = function.__doc__
            return function(value)
        return new_func
    check_type.__doc__ = check_type_.__doc__
    return check_type_


class MacroSaver:

    __Macros: list = []

    def search(self, name_macro: str):
        """if it finds a matching name it will return it, and it's index otherwise
        it will return None"""
        index = -1
        for m in self.__Macros:
            index += 1
            if name_macro == m.name:
                return m.name, index

    @check_type(Macro)
    def check_unique(self, macro: Macro):

        result = self.search(macro.name)
        if result[0] is not None:
            raise errors.UniqueNameError(macro.name, result[0])

    @check_type(Macro)
    def __add__(self, macro: Macro):
        self.__Macros.append(macro)

    def __sub__(self, name: str):

        result = self.search(name)
        if result is None:
            raise IndexError("the "+str(name)+" is not defined.")
        else:
            self.__Macros.pop(result[1])

