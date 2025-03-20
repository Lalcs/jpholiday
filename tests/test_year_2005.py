import datetime
import unittest

import jpholiday


class TestYear2005(unittest.TestCase):
    def test_holiday(self):
        """
        2005年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 1, 10)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 3, 21)), '春分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 7, 18)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 9, 19)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2005, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2005年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2005, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2005, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2005, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2005, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2005, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2005, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2005, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2005, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2005, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2005, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2005, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2005, 12)), 1)

    def test_count_year(self):
        """
        2005年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2005)), 16)
