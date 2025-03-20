import datetime
import unittest

import jpholiday


class TestYear1999(unittest.TestCase):
    def test_holiday(self):
        """
        1999年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 3, 22)), '春分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 10, 11)), '体育の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1999, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        1999年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1999, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1999, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1999, 3)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1999, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1999, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1999, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1999, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1999, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1999, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1999, 10)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1999, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1999, 12)), 1)

    def test_count_year(self):
        """
        1999年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1999)), 17)
