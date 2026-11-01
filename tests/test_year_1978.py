import datetime
import unittest

import jpholiday


class TestYear1978(unittest.TestCase):
    def test_holiday(self):
        """
        1978年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1978, 1, 1)), "元日")
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 1, 2)), "元日 振替休日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 1, 15)), "成人の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 1, 16)), "成人の日 振替休日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 2, 11)), "建国記念の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 3, 21)), "春分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 4, 29)), "天皇誕生日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 5, 3)), "憲法記念日"
        )
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1978, 5, 4)), None)
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 5, 5)), "こどもの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 9, 15)), "敬老の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 9, 23)), "秋分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 10, 10)), "体育の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 11, 3)), "文化の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1978, 11, 23)), "勤労感謝の日"
        )

    def test_count_month(self):
        """
        1978年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1978, 1)), 4)
        self.assertEqual(len(jpholiday.month_holidays(1978, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1978, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1978, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1978, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1978, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1978, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1978, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1978, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1978, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1978, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1978, 12)), 0)

    def test_count_year(self):
        """
        1978年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1978)), 14)
