import datetime
import unittest

import jpholiday


class TestYear1998(unittest.TestCase):
    def test_holiday(self):
        """
        1998年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 5, 4)), '憲法記念日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 5, 6)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1998, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        1998年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1998, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1998, 2)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1998, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1998, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1998, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1998, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1998, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1998, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1998, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1998, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1998, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1998, 12)), 1)

    def test_count_year(self):
        """
        1998年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1998)), 15)
