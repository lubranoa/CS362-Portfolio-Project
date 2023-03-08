import unittest
from task import conv_num, conv_endian


class TestCase(unittest.TestCase):

    # Begin conv_num tests
    def test1_conv(self):
        number = '12345'
        self.assertEqual(conv_num(number), 12345)

    def test2_conv(self):
        number = '-12345'
        self.assertEqual(conv_num(number), -12345)

    def test3_conv(self):
        number = '12.345'
        self.assertEqual(conv_num(number), 12.345)

    def test4_conv(self):
        number = '-12.345'
        self.assertEqual(conv_num(number), -12.345)

    def test5_conv(self):
        number = '.45'
        self.assertEqual(conv_num(number), 0.45)

    def test6_conv(self):
        number = '0xAD4'
        self.assertEqual(conv_num(number), 2772)

    def test7_conv(self):
        number = '0xAZ4'
        self.assertEqual(conv_num(number), None)

    # -----------------------------------------------------------------
    # Test Driven Development for conv_endian()
    #
    # -----------------------------------------------------------------

    # Verifies if the number 0 is returned correctly
    def test1_conv_end(self):
        number = 0
        self.assertEqual(conv_endian(number), '00')

    # Verifies if the number 6 is returned properly
    def test2_conv_end(self):
        number = 6
        self.assertEqual(conv_endian(number), '06')

    # Verifies if the number 9 is returned properly
    def test3_conv_end(self):
        number = 9
        self.assertEqual(conv_endian(number), '09')

    # Verifies if the number 10 is returned properly
    def test4_conv_end(self):
        number = 10
        self.assertEqual(conv_endian(number), '0A')

    # Verifies if the number 15 is returned properly
    def test5_conv_end(self):
        number = 15
        self.assertEqual(conv_endian(number), '0F')

    # Verifies if the number 16 is returned properly
    def test6_conv_end(self):
        number = 16
        self.assertEqual(conv_endian(number), '10')

    # Verifies if the number 100 is returned properly
    def test7_conv_end(self):
        number = 100
        self.assertEqual(conv_endian(number), '64')

    # Verifies if the number 196 is returned properly
    def test8_conv_end(self):
        number = 196
        self.assertEqual(conv_endian(number), 'C4')

    # Verifies if the number 255 is returned properly
    def test9_conv_end(self):
        number = 255
        self.assertEqual(conv_endian(number), 'FF')

    # Verifies if the number 256 is returned properly
    def test10_conv_end(self):
        number = 256
        self.assertEqual(conv_endian(number), '01 00')

    # Verifies if the number 65535 is returned properly
    def test11_conv_end(self):
        number = 65535
        self.assertEqual(conv_endian(number), 'FF FF')

    # Verifies if the number 954786 is returned properly
    def test12_conv_end(self):
        number = 954786
        self.assertEqual(conv_endian(number), '0E 91 A2')

    # Verifies if the number 99999999 is returned properly
    def test13_conv_end(self):
        number = 99999999
        self.assertEqual(conv_endian(number), '05 F5 E0 FF')

    # Verifies if the number -1 is returned properly
    def test14_conv_end(self):
        number = -1
        self.assertEqual(conv_endian(number), '-01')


if __name__ == '__main__':
    unittest.main(verbosity=2)
