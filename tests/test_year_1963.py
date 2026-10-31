import datetime
import unittest

import jpholiday


class TestYear1963(unittest.TestCase):
    def test_holiday(self):
        """
        1963年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 9, 24)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1963, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1963年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1963, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1963, 2)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1963, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1963, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1963, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1963, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1963, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1963, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1963, 9)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1963, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1963, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1963, 12)), 0)

    def test_count_year(self):
        """
        1963年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1963)), 9)
