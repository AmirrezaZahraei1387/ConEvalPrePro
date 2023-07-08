import dataclasses
import ceval.errors as errors


@dataclasses.dataclass
class Macro:
    """this is a simple data class that uses the
    name and the value of a specific macro to save it."""
    name: str
    value: str


def check_type(type_):
    def check_type_(function):
        def new_func(self, value):
            if not isinstance(value, type_):
                raise TypeError(str(value)+" is not "+str(type_)+" object.")
            new_func.__doc__ = function.__doc__
            return function(self, value)
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

    def check_unique(self, macro):

        result = self.search(macro)
        if result is not None:
            raise errors.UniqueNameError(macro, result[0])

    @check_type(Macro)
    def __iadd__(self, macro: Macro):

        self.check_unique(macro.name)
        self.__Macros.append(macro)
        return self

    def __isub__(self, name: str):

        result = self.search(name)
        if result is None:
            raise IndexError("the "+str(name)+" is not defined.")
        else:
            self.__Macros.pop(result[1])

        return self



