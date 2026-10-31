import datetime
import unittest

import jpholiday


class TestYear1956(unittest.TestCase):
    def test_holiday(self):
        """
        1956年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1956, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1956年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1956, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1956, 2)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1956, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1956, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1956, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1956, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1956, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1956, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1956, 9)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1956, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1956, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1956, 12)), 0)

    def test_count_year(self):
        """
        1956年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1956)), 9)
