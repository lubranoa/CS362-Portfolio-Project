import unittest
from task import my_datetime
import datetime

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test1_datetime(self):
        num_sec = 123456789
        date = datetime.datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(my_datetime(num_sec), date)

    def test2_datetime(self):
        num_sec = 9876543210
        date = datetime.datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(my_datetime(num_sec), date)

    def test3_datetime(self):
        num_sec = 201653971
        date = datetime.datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(my_datetime(num_sec), date)

    def test4_datetime(self):
        num_sec = 1245639842
        date = datetime.datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(my_datetime(num_sec), date)

    def test5_datetime(self):
        num_sec = 201653971200
        date = datetime.datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(my_datetime(num_sec), date)


if __name__ == '__main__':
    unittest.main()
