import datetime
import unittest

import jpholiday


class TestYear2012(unittest.TestCase):
    def test_holiday(self):
        """
        2012年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 1, 2)), '元日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 1, 9)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 4, 29)), '昭和の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 4, 30)), '昭和の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 5, 4)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 7, 16)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 9, 17)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 9, 22)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 10, 8)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 12, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2012, 12, 24)), '天皇誕生日 振替休日')

    def test_count_month(self):
        """
        2012年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2012, 1)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2012, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2012, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2012, 4)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2012, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2012, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2012, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2012, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2012, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2012, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2012, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2012, 12)), 2)

    def test_count_year(self):
        """
        2012年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2012)), 18)
