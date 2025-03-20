import datetime
import unittest

import jpholiday


class TestYear2011(unittest.TestCase):
    def test_holiday(self):
        """
        2011年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 1, 10)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 7, 18)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 9, 19)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2011, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2011年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2011, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2011, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2011, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2011, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2011, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2011, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2011, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2011, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2011, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2011, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2011, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2011, 12)), 1)

    def test_count_year(self):
        """
        2011年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2011)), 15)
