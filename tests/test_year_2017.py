import datetime
import unittest

import jpholiday


class TestYear2017(unittest.TestCase):
    def test_holiday(self):
        """
        2017年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 1, 2)), '元日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 1, 9)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 7, 17)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 9, 18)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 10, 9)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2017年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2017, 1)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2017, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2017, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2017, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2017, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2017, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2017, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2017, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2017, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2017, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2017, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2017, 12)), 1)

    def test_count_year(self):
        """
        2017年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2017)), 17)
