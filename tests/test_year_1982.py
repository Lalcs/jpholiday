import datetime
import unittest

import jpholiday


class TestYear1982(unittest.TestCase):
    def test_holiday(self):
        """
        1982年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1982, 1, 1)), "元日")
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 1, 15)), "成人の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 2, 11)), "建国記念の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 3, 21)), "春分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 3, 22)), "春分の日 振替休日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 4, 29)), "天皇誕生日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 5, 3)), "憲法記念日"
        )
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1982, 5, 4)), None)
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 5, 5)), "こどもの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 9, 15)), "敬老の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 9, 23)), "秋分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 10, 10)), "体育の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 10, 11)), "体育の日 振替休日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 11, 3)), "文化の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1982, 11, 23)), "勤労感謝の日"
        )

    def test_count_month(self):
        """
        1982年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1982, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1982, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1982, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1982, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1982, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1982, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1982, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1982, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1982, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1982, 10)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1982, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1982, 12)), 0)

    def test_count_year(self):
        """
        1982年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1982)), 14)
