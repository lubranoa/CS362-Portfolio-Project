import unittest
from task import conv_num


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


if __name__ == '__main__':
    unittest.main()
