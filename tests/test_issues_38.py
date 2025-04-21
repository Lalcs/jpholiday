import calendar
import datetime
import unittest

import jpholiday


class TestIssues38(unittest.TestCase):

    def test_main(self):
        """
        calendar.setfirstweekday による祝日判定の不具合
        https://github.com/Lalcs/jpholiday/issues/38
        """
        calendar.setfirstweekday(calendar.SUNDAY)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 15)), True)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 16)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 17)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 18)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 19)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 20)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 21)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 22)), False)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 23)), True)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2025, 9, 24)), False)
