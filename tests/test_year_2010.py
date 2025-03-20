import datetime
import unittest

import jpholiday


class TestYear2010(unittest.TestCase):
    def test_holiday(self):
        """
        2010年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 1, 11)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 3, 22)), '春分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 7, 19)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 9, 20)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 10, 11)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2010, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2010年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2010, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2010, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2010, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2010, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2010, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2010, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2010, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2010, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2010, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2010, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2010, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2010, 12)), 1)

    def test_count_year(self):
        """
        2010年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2010)), 16)
