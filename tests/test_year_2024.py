import datetime
import unittest

import jpholiday


class TestYear2024(unittest.TestCase):
    def test_holiday(self):
        """
        2024年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 1, 8)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 2, 12)), '建国記念の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 5, 6)), 'こどもの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 7, 15)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 8, 12)), '山の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 9, 16)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 9, 22)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 9, 23)), '秋分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 10, 14)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 11, 4)), '文化の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2024, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2024年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2024, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2024, 2)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2024, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2024, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2024, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2024, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2024, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2024, 8)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2024, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2024, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2024, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2024, 12)), 0)

    def test_count_year(self):
        """
        2024年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2024)), 21)
