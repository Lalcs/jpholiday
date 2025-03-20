import datetime
import unittest

import jpholiday


class TestYear2014(unittest.TestCase):
    def test_holiday(self):
        """
        2014年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 1, 13)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 5, 6)), 'みどりの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 7, 21)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 10, 13)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 11, 24)), '勤労感謝の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2014, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2014年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2014, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2014, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2014, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2014, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2014, 5)), 4)
        self.assertEqual(len(jpholiday.month_holidays(2014, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2014, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2014, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2014, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2014, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2014, 11)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2014, 12)), 1)

    def test_count_year(self):
        """
        2014年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2014)), 17)
