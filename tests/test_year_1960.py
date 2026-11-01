import datetime
import unittest

import jpholiday


class TestYear1960(unittest.TestCase):
    def test_holiday(self):
        """
        1960年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1960, 1, 1)), "元日")
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 1, 15)), "成人の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 3, 20)), "春分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 4, 29)), "天皇誕生日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 5, 3)), "憲法記念日"
        )
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1960, 5, 4)), None)
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 5, 5)), "こどもの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 9, 23)), "秋分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 11, 3)), "文化の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1960, 11, 23)), "勤労感謝の日"
        )

    def test_count_month(self):
        """
        1960年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1960, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1960, 2)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1960, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1960, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1960, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1960, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1960, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1960, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1960, 9)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1960, 10)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1960, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1960, 12)), 0)

    def test_count_year(self):
        """
        1960年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1960)), 9)
