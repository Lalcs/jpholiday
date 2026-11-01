import datetime
import unittest

import jpholiday


class TestYear1994(unittest.TestCase):
    def test_holiday(self):
        """
        1994年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1994, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        1994年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1994, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1994, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1994, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1994, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1994, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1994, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1994, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1994, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1994, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1994, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1994, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1994, 12)), 1)

    def test_count_year(self):
        """
        1994年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1994)), 14)
