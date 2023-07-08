import unittest
from ceval.defines_saver import check_type, MacroSaver, Macro
import ceval

obj = MacroSaver()

macro_1 = Macro("AH", "5")
macro_2 = Macro("AI", "5")
macro_3 = Macro("AL", "5")

obj += macro_1
obj += macro_2
obj += macro_3


class test(unittest.TestCase):

    @check_type(int)
    def check_type_test(self, number):
        return number * 2

    def test_check_type_error_raising(self):

        try:
            self.check_type_test("kkk")
        except TypeError:
            a = True
        else:
            a = False

        self.assertEqual(a, True)

    def test_check_type_error_raising_2(self):

        try:
            self.check_type_test(5)
        except TypeError:
            a = False
        else:
            a = True

        self.assertEqual(a, True)

    def test_search_class_MacroSaver(self):

        result = obj.search("AH")
        result_1 = obj.search("hh")

        result_all = [result, result_1]
        self.assertEqual(result_all, [("AH", 0), None])

    def test_check_unique_class_MacroSver(self):

        result = obj.check_unique("gg")
        self.assertEqual(result, None)

    def test_check_unique_class_MacroSver_1(self):

        try:
            obj.check_unique("AL")
        except ceval.errors.UniqueNameError:
            a = True
        else:
            a = False

        self.assertEqual(a, True)

    def test__iadd__(self):
        global obj

        mac = Macro("AI", "g")

        try:
            obj += mac
        except ceval.errors.UniqueNameError:
            a = True
        else:
            a = False

        self.assertEqual(a, True)

    def test__iadd___1(self):

        global obj

        mac = Macro("A", "hh")
        obj += mac

        result = obj.search("A")

        self.assertEqual(result is not None, True)

    def test__sub__(self):

        global obj

        try:
            obj -= "gfff"
        except IndexError:
            a = True
        else:
            a = False
        # "the given name does not exist and error is given"
        self.assertEqual(a, True)

    def test__sub___1(self):

        global obj

        obj -= "AI"
        result = obj.search("AI")
        # "the Macro that is excepted is deleted"
        self.assertEqual(result, None)
