import datetime
import unittest

import jpholiday


class TestYear2009(unittest.TestCase):
    def test_holiday(self):
        """
        2009年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 1, 12)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 5, 6)), '憲法記念日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 9, 21)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 9, 22)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 10, 12)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2009, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2009年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2009, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2009, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2009, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2009, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2009, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2009, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2009, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2009, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2009, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2009, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2009, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2009, 12)), 1)

    def test_count_year(self):
        """
        2009年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2009)), 17)
