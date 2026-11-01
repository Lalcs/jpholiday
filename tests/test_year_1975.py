import datetime
import unittest

import jpholiday


class TestYear1975(unittest.TestCase):
    def test_holiday(self):
        """
        1975年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1975, 1, 1)), "元日")
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 1, 15)), "成人の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 2, 11)), "建国記念の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 3, 21)), "春分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 4, 29)), "天皇誕生日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 5, 3)), "憲法記念日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 5, 5)), "こどもの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 9, 15)), "敬老の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 9, 24)), "秋分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 10, 10)), "体育の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 11, 3)), "文化の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 11, 23)), "勤労感謝の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1975, 11, 24)),
            "勤労感謝の日 振替休日",
        )

    def test_count_month(self):
        """
        1975年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1975, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1975, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1975, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1975, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1975, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1975, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1975, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1975, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1975, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1975, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1975, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1975, 12)), 0)

    def test_count_year(self):
        """
        1975年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1975)), 13)
