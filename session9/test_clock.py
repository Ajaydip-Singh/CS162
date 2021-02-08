from clock import ClockIterator
import unittest
class TestClock(unittest.TestCase):

    def test_check_1(self):
        clock = ClockIterator()
        c = 1
        for time in clock:
            if c == 1:
                result = time
        self.assertEqual(result, '00:00')


    def test_check_60(self):
        clock = ClockIterator()
        c = 1
        for time in clock:
            if c == 60:
                result = time
            c += 1
        self.assertEqual(result, '00:59')


    def test_check_61(self):
        clock = ClockIterator()
        c = 1
        for time in clock:
            if c == 61:
                result = time
            c += 1
        self.assertEqual(result, '01:00')


    def test_check_1440(self):
        clock = ClockIterator()
        c = 1
        for time in clock:
            if c == 60:
                result = time
            c += 1
        self.assertEqual(result, '23:59')
        

    def test_check_1441(self):
        clock = ClockIterator()
        c = 1
        for time in clock:
            if c == 1441:
                result = time
            c += 1
        self.assertEqual(result, '00:00')
