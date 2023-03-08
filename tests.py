import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    # Begin conv_num tests
    def test1_conv_num(self):
        number = '12345'
        self.assertEqual(conv_num(number), 12345)

    def test2_conv_num(self):
        number = '-12345'
        self.assertEqual(conv_num(number), -12345)

    def test3_conv_num(self):
        number = '12.345'
        self.assertEqual(conv_num(number), 12.345)

    def test4_conv_num(self):
        number = '-12.345'
        self.assertEqual(conv_num(number), -12.345)

    def test5_conv_num(self):
        number = '.45'
        self.assertEqual(conv_num(number), 0.45)

    def test6_conv_num(self):
        number = '0xAD4'
        self.assertEqual(conv_num(number), 2772)

    def test7_conv_num(self):
        number = '0xAZ4'
        self.assertEqual(conv_num(number), None)

    def test8_conv_num(self):
        number = '12312341235'
        self.assertEqual(conv_num(number), 12312341235)

    def test9_conv_num(self):
        number = '-12312A5'
        self.assertEqual(conv_num(number), None)

    def test10_conv_num(self):
        number = '--1212'
        self.assertEqual(conv_num(number), None)

    def test11_conv_num(self):
        number = '-456-12'
        self.assertEqual(conv_num(number), None)


if __name__ == '__main__':
    unittest.main()
