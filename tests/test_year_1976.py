import datetime
import unittest

import jpholiday


class TestYear1976(unittest.TestCase):
    def test_holiday(self):
        """
        1976年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 10, 11)), '体育の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1976, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1976年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1976, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1976, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1976, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1976, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1976, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1976, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1976, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1976, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1976, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1976, 10)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1976, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1976, 12)), 0)

    def test_count_year(self):
        """
        1976年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1976)), 13)
