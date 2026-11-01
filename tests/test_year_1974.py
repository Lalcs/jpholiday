import datetime
import unittest

import jpholiday


class TestYear1974(unittest.TestCase):
    def test_holiday(self):
        """
        1974年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 5, 6)), 'こどもの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 9, 16)), '敬老の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 11, 4)), '文化の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1974, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1974年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1974, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1974, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1974, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1974, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1974, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1974, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1974, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1974, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1974, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1974, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1974, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1974, 12)), 0)

    def test_count_year(self):
        """
        1974年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1974)), 15)
