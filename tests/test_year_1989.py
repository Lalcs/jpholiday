import datetime
import unittest

import jpholiday


class TestYear1989(unittest.TestCase):
    def test_holiday(self):
        """
        1989年祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 1, 1)), '元日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 1, 2)), '元日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 1, 15)), '成人の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 1, 16)), '成人の日 振替休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 2, 11)), '建国記念の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 2, 24)), '昭和天皇の大喪の礼')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 3, 21)), '春分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 4, 29)), 'みどりの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 5, 3)), '憲法記念日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 5, 4)), '国民の休日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 5, 5)), 'こどもの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 9, 15)), '敬老の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 9, 23)), '秋分の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 10, 10)), '体育の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 11, 3)), '文化の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 11, 23)), '勤労感謝の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 12, 23)), '天皇誕生日')

    def test_count_month(self):
        """
        1989年月祝日数
        """
        self.assertEqual(len(jpholiday.month_holidays(1989, 1)), 4)
        self.assertEqual(len(jpholiday.month_holidays(1989, 2)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1989, 3)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1989, 4)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1989, 5)), 3)
        self.assertEqual(len(jpholiday.month_holidays(1989, 6)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1989, 7)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1989, 8)), 0)
        self.assertEqual(len(jpholiday.month_holidays(1989, 9)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1989, 10)), 1)
        self.assertEqual(len(jpholiday.month_holidays(1989, 11)), 2)
        self.assertEqual(len(jpholiday.month_holidays(1989, 12)), 1)

    def test_count_year(self):
        """
        1989年祝日数
        """
        self.assertEqual(len(jpholiday.year_holidays(1989)), 17)
