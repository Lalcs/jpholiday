import datetime
import unittest

import jpholiday


class TestYear2007(unittest.TestCase):
    def test_holiday(self):
        """
        2007年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 1, 8)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 2, 12)), '建国記念の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 4, 30)), '昭和の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 7, 16)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 9, 17)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 9, 24)), '秋分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 10, 8)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 12, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2007, 12, 24)), '天皇誕生日 振替休日')

    def test_count_month(self):
        """
        2007年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2007, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2007, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2007, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2007, 4)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2007, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2007, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2007, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2007, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2007, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2007, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2007, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2007, 12)), 2)

    def test_count_year(self):
        """
        2007年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2007)), 19)
