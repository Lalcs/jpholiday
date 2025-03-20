import datetime
import unittest

import jpholiday


class TestYear2006(unittest.TestCase):
    def test_holiday(self):
        """
        2006年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 1, 2)), '元日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 1, 9)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 7, 17)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 9, 18)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 10, 9)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2006, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2006年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2006, 1)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2006, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2006, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2006, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2006, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2006, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2006, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2006, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2006, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2006, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2006, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2006, 12)), 1)

    def test_count_year(self):
        """
        2006年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2006)), 16)
