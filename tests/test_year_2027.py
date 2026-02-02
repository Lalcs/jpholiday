import datetime
import unittest

import jpholiday


class TestYear2027(unittest.TestCase):
    def test_holiday(self):
        """
        2027年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 1, 11)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 3, 22)), '春分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 7, 19)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 9, 20)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 10, 11)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2027, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2027年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2027, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2027, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2027, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2027, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2027, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2027, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2027, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2027, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2027, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2027, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2027, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2027, 12)), 0)

    def test_count_year(self):
        """
        2027年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2027)), 17)
