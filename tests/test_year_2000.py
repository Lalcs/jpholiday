import datetime
import unittest

import jpholiday


class TestYear2000(unittest.TestCase):
    def test_holiday(self):
        """
        2000年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 1, 10)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 10, 9)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2000, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        2000年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2000, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2000, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2000, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2000, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2000, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2000, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2000, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2000, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2000, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2000, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2000, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2000, 12)), 1)

    def test_count_year(self):
        """
        2000年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2000)), 15)
