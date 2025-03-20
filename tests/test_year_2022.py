import datetime
import unittest

import jpholiday


class TestYear2022(unittest.TestCase):
    def test_holiday(self):
        """
        2022年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 1, 10)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 7, 18)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 9, 19)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 10, 10)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2022, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2022年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2022, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2022, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2022, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2022, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2022, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2022, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2022, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2022, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2022, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2022, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2022, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2022, 12)), 0)

    def test_count_year(self):
        """
        2022年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2022)), 16)
