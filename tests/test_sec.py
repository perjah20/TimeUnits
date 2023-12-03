import unittest

from timeunits import Sec


class TimeUnitTests(unittest.TestCase):

    def test_create_sec(self):
        sec = Sec(1)
        self.assertEqual(sec.v, 1)
        self.assertEqual(sec.multiple_of_a_second(), 0)

    def test_check_float(self):
        sec = Sec(1.5)
        with self.subTest("Testing __float__"):
            self.assertEqual(float(sec), 1.5)
        with self.subTest("Testing .value"):
            self.assertEqual(sec.v, 1.5)
        with self.subTest("Testing int"):
            self.assertEqual(int(sec), 1)

    def test_conversion_to_milliseconds(self):
        sec = Sec(1)
        self.assertEqual(1000, float(sec.to_milli()))

    def test_conversion_to_microseconds(self):
        sec = Sec(1)
        self.assertEqual(1000000, float(sec.to_micro()))

    def test_conversion_to_nanoseconds(self):
        sec = Sec(1)
        self.assertEqual(1000000000, float(sec.to_nano()))

    def test_conversion_to_deciseconds(self):
        sec = Sec(1)
        self.assertEqual(10, float(sec.to_deci()))

    def test_conversion_to_centiseconds(self):
        sec = Sec(1)
        self.assertEqual(100, float(sec.to_centi()))

    def test_conversion_to_decaseconds(self):
        sec = Sec(1)
        self.assertEqual(0.1, float(sec.to_deca()))

    def test_v_setter(self):
        sec = Sec(1)
        sec.v = 2
        self.assertEqual(sec.v, 2)

    def test_v_setter_invalid(self):
        sec = Sec(1)
        with self.assertRaises(ValueError):
            sec.v = -1

    def test_v_setter_invalid_type(self):
        sec = Sec(1)
        with self.assertRaises(TypeError):
            sec.v = "1"

    def test_convert_to_sec(self):
        sec = Sec(1)
        self.assertEqual(1, float(sec.to_sec()))

    def test_convert_to_mili_and_back(self):
        sec = Sec(1)
        self.assertEqual(1, float(sec.to_milli().to_sec()))

    def test_str_representation(self):
        sec = Sec(1)
        self.assertEqual("1.0 s", str(sec))

    def test_addition(self):
        sec = Sec(1)
        self.assertEqual(2, float(sec + sec))

    def test_subtraction(self):
        sec = Sec(1)
        self.assertEqual(0, float(sec - sec))

    def test_multiplication(self):
        sec = Sec(1)
        self.assertEqual(2, float(sec * 2))

    def test_division(self):
        sec = Sec(1)
        self.assertEqual(0.5, float(sec / 2))

    def test_divion_by_0(self):
        sec = Sec(1)
        with self.assertRaises(ZeroDivisionError):
            sec / 0





if __name__ == '__main__':
    unittest.main()
