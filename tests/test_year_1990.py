import datetime
import unittest

import jpholiday


class TestYear1990(unittest.TestCase):
    def test_holiday(self):
        """
        1990年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 2, 12)), '建国記念の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 4, 30)), 'みどりの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 9, 24)), '秋分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 11, 12)), '即位の礼正殿の儀')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 12, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 12, 24)), '天皇誕生日 振替休日')

    def test_count_month(self):
        """
        1990年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1990, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1990, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1990, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1990, 4)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1990, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1990, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1990, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1990, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1990, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1990, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1990, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1990, 12)), 2)

    def test_count_year(self):
        """
        1990年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1990)), 19)
