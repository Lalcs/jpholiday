import datetime
import unittest

import jpholiday


class TestYear2016(unittest.TestCase):
    def test_holiday(self):
        """
        2016年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 1, 11)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 3, 21)), '春分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 7, 18)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 9, 19)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 9, 22)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2016年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2016, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2016, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2016, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2016, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2016, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2016, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2016, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2016, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2016, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2016, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2016, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2016, 12)), 1)

    def test_count_year(self):
        """
        2016年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2016)), 17)
