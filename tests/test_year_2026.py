import datetime
import unittest

import jpholiday


class TestYear2026(unittest.TestCase):
    def test_holiday(self):
        """
        2026年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 1, 12)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 5, 6)), '憲法記念日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 9, 21)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 9, 22)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 10, 12)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2026, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2026年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2026, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2026, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2026, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2026, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2026, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2026, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2026, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2026, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2026, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2026, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2026, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2026, 12)), 0)

    def test_count_year(self):
        """
        2026年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2026)), 18)
