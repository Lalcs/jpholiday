import datetime
import unittest

import jpholiday


class TestYear1958(unittest.TestCase):
    def test_holiday(self):
        """
        1958年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1958, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1958年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1958, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1958, 2)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1958, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1958, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1958, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1958, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1958, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1958, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1958, 9)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1958, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1958, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1958, 12)), 0)

    def test_count_year(self):
        """
        1958年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1958)), 9)
