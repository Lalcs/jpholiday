import datetime
import unittest

import jpholiday


class TestYear2008(unittest.TestCase):
    def test_holiday(self):
        """
        2008年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 1, 14)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 5, 6)), 'みどりの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 7, 21)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 10, 13)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 11, 24)), '勤労感謝の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2008, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2008年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2008, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2008, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2008, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2008, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2008, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2008, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2008, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2008, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2008, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2008, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2008, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2008, 12)), 1)

    def test_count_year(self):
        """
        2008年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2008)), 17)
