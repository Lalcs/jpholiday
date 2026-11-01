import datetime
import unittest

import jpholiday


class TestYear1986(unittest.TestCase):
    def test_holiday(self):
        """
        1986年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1986, 1, 1)), "元日")
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 1, 15)), "成人の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 2, 11)), "建国記念の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 3, 21)), "春分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 4, 29)), "天皇誕生日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 5, 3)), "憲法記念日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 5, 5)), "こどもの日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 9, 15)), "敬老の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 9, 23)), "秋分の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 10, 10)), "体育の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 11, 3)), "文化の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 11, 23)), "勤労感謝の日"
        )
        self.assertEqual(
            jpholiday.is_holiday_name(datetime.date(1986, 11, 24)),
            "勤労感謝の日 振替休日",
        )

    def test_count_month(self):
        """
        1986年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1986, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1986, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1986, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1986, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1986, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1986, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1986, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1986, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1986, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1986, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1986, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1986, 12)), 0)

    def test_count_year(self):
        """
        1986年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1986)), 13)
