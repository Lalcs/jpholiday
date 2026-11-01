import datetime
import unittest

import jpholiday


class TestYear1968(unittest.TestCase):
    def test_holiday(self):
        """
        1968年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1968, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1968年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1968, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1968, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1968, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1968, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1968, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1968, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1968, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1968, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1968, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1968, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1968, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1968, 12)), 0)

    def test_count_year(self):
        """
        1968年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1968)), 12)
