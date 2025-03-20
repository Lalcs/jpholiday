import datetime
import unittest

import jpholiday


class TestYear1997(unittest.TestCase):
    def test_holiday(self):
        """
        1997年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 7, 21)), '海の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 11, 24)), '勤労感謝の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1997, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        1997年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1997, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1997, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1997, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1997, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1997, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1997, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1997, 7)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1997, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1997, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1997, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1997, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1997, 12)), 1)

    def test_count_year(self):
        """
        1997年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1997)), 16)
