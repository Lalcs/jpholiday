import datetime
import unittest

import jpholiday


class TestYear1993(unittest.TestCase):
    def test_holiday(self):
        """
        1993年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1993, 1, 1)), "元日")
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 1, 15)), "成人の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 2, 11)), "建国記念の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 3, 20)), "春分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 4, 29)), "みどりの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 5, 3)), "憲法記念日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 5, 4)), "国民の休日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 5, 5)), "こどもの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 6, 9)),
            "皇太子・皇太子徳仁親王の結婚の儀",
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 9, 15)), "敬老の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 9, 23)), "秋分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 10, 10)), "体育の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 10, 11)), "体育の日 振替休日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 11, 3)), "文化の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 11, 23)), "勤労感謝の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1993, 12, 23)), "天皇誕生日"
        )

    def test_count_month(self):
        """
        1993年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1993, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1993, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1993, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1993, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1993, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1993, 6)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1993, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1993, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1993, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1993, 10)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1993, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1993, 12)), 1)

    def test_count_year(self):
        """
        1993年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1993)), 16)
