import datetime
import unittest

import jpholiday


class TestYear2023(unittest.TestCase):
    def test_holiday(self):
        """
        2023年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 1, 2)), '元日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 1, 9)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 7, 17)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 8, 11)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 9, 18)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 10, 9)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2023, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2023年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2023, 1)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2023, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2023, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2023, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2023, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2023, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2023, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2023, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2023, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2023, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2023, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2023, 12)), 0)

    def test_count_year(self):
        """
        2023年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2023)), 17)
