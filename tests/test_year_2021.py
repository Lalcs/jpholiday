import datetime
import unittest

import jpholiday


class TestYear2021(unittest.TestCase):
    def test_holiday(self):
        """
        2021年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 1, 11)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 7, 22)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 7, 23)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 8, 8)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 8, 9)), '山の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 9, 20)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2021, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2021年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2021, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2021, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2021, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2021, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2021, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2021, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2021, 7)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2021, 8)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2021, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2021, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2021, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2021, 12)), 0)

    def test_count_year(self):
        """
        2021年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2021)), 17)
