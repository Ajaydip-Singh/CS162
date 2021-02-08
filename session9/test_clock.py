from clock import ClockIterator
import unittest
class TestClock(unittest.TestCase):

    clock = ClockIterator()

    def test_check_1(self):
        c = 1
        for time in self.clock:
            if c == 1:
                result = time
                break
        self.assertEqual(result, '00:00')


    def test_check_60(self):
        c = 1
        for time in self.clock:
            if c == 60:
                result = time
                break
            c += 1
        self.assertEqual(result, '00:59')


    def test_check_61(self):
        c = 1
        for time in self.clock:
            if c == 61:
                result = time
                break
            c += 1
        self.assertEqual(result, '01:00')


    def test_check_1440(self):
        c = 1
        for time in self.clock:
            if c == 1440:
                result = time
                break
            c += 1
        self.assertEqual(result, '23:59')
        

    def test_check_1441(self):
        c = 1
        for time in self.clock:
            if c == 1441:
                result = time
                break
            c += 1
        self.assertEqual(result, '00:00')
