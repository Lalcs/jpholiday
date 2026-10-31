import datetime
import unittest

import jpholiday


class TestYear1948(unittest.TestCase):
    def test_holiday(self):
        """
        1948年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 1, 1)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 1, 15)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 3, 21)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 4, 29)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 5, 3)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 5, 5)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1948, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1948年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1948, 1)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 2)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 3)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 4)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 5)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 9)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1948, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1948, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1948, 12)), 0)

    def test_count_year(self):
        """
        1948年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1948)), 3)
