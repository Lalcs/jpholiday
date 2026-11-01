import datetime
import unittest

import jpholiday


class TestYear1995(unittest.TestCase):
    def test_holiday(self):
        """
        1995年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 1, 2)), '元日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 1, 16)), '成人の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1995, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        1995年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1995, 1)), 4)
        self.assertEqual(len(jpholiday.month_holidays(1995, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1995, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1995, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1995, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1995, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1995, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1995, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1995, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1995, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1995, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1995, 12)), 1)

    def test_count_year(self):
        """
        1995年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1995)), 16)
