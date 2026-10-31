import datetime
import unittest

import jpholiday


class TestYear1966(unittest.TestCase):
    def test_holiday(self):
        """
        1966年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1966, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1966年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1966, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1966, 2)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1966, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1966, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1966, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1966, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1966, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1966, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1966, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1966, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1966, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1966, 12)), 0)

    def test_count_year(self):
        """
        1966年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1966)), 11)
