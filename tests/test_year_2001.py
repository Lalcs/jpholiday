import datetime
import unittest

import jpholiday


class TestYear2001(unittest.TestCase):
    def test_holiday(self):
        """
        2001年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 1, 8)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 2, 12)), '建国記念の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 3, 20)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 4, 30)), 'みどりの日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 7, 20)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 9, 24)), '秋分の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 10, 8)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 12, 23)), '天皇誕生日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2001, 12, 24)), '天皇誕生日 振替休日')

    def test_count_month(self):
        """
        2001年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(2001, 1)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2001, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2001, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2001, 4)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2001, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2001, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2001, 7)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2001, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(2001, 9)), 3)
        self.assertEqual(len(jpholiday.month_holidays(2001, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(2001, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(2001, 12)), 2)

    def test_count_year(self):
        """
        2001年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(2001)), 19)
