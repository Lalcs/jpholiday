import datetime
import unittest

import jpholiday


class TestYear1988(unittest.TestCase):
    def test_holiday(self):
        """
        1988年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 3, 21)), '春分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1988, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1988年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1988, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1988, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1988, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1988, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1988, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1988, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1988, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1988, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1988, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1988, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1988, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1988, 12)), 0)

    def test_count_year(self):
        """
        1988年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1988)), 14)
