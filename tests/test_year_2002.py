import datetime
import unittest

import jpholiday


class TestYear2002(unittest.TestCase):
    def test_holiday(self):
        """
        2002年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 1, 14)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 5, 6)), 'こどもの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 9, 16)), '敬老の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 10, 14)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 11, 4)), '文化の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2002, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2002年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2002, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2002, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2002, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2002, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2002, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2002, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2002, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2002, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2002, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2002, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2002, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2002, 12)), 1)

    def test_count_year(self):
        """
        2002年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2002)), 18)
