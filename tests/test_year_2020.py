import datetime
import unittest

import jpholiday


class TestYear2020(unittest.TestCase):
    def test_holiday(self):
        """
        2020年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 1, 13)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 24)), '天皇誕生日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 5, 6)), '憲法記念日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 7, 23)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 7, 24)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 8, 10)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 9, 21)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 9, 22)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        2020年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2020, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2020, 2)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2020, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2020, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2020, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2020, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2020, 7)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2020, 8)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2020, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2020, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2020, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2020, 12)), 0)

    def test_count_year(self):
        """
        2020年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2020)), 18)
