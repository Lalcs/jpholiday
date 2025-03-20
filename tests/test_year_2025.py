import datetime
import unittest

import jpholiday


class TestYear2025(unittest.TestCase):
    def test_holiday(self):
        """
        2025年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 1, 13)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 2, 24)), '天皇誕生日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 5, 6)), 'みどりの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 7, 21)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 10, 13)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2025, 11, 24)), '勤労感謝の日 振替休日')

    def test_count_month(self):
        """
        2025年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2025, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2025, 2)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2025, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2025, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2025, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2025, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2025, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2025, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2025, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2025, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2025, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2025, 12)), 0)

    def test_count_year(self):
        """
        2025年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2025)), 19)
