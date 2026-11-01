import datetime
import unittest

import jpholiday


class TestYear1979(unittest.TestCase):
    def test_holiday(self):
        """
        1979年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 2, 12)), '建国記念の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 4, 29)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 4, 30)), '天皇誕生日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 5, 4)), None)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 9, 24)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1979, 11, 23)), '勤労感謝の日')

    def test_count_month(self):
        """
        1979年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1979, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1979, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1979, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1979, 4)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1979, 5)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1979, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1979, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1979, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1979, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1979, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1979, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1979, 12)), 0)

    def test_count_year(self):
        """
        1979年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1979)), 14)
