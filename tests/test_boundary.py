import datetime
import unittest

import jpholiday
from jpholiday import JPHoliday


class TestBoundary(unittest.TestCase):
    """
    datetime で扱える日付の上限・下限での動作
    """

    def test_is_holiday_max(self):
        self.assertEqual(jpholiday.is_holiday(datetime.date.max), False)
        self.assertEqual(jpholiday.is_holiday(datetime.datetime.max), False)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date.max), None)

    def test_is_holiday_min(self):
        self.assertEqual(jpholiday.is_holiday(datetime.date.min), False)
        self.assertEqual(jpholiday.is_holiday(datetime.datetime.min), False)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date.min), None)

    def test_year_holidays_max(self):
        holidays = jpholiday.year_holidays(9999)
        self.assertIn((datetime.date(9999, 1, 1), "元日"), holidays)
        self.assertIn((datetime.date(9999, 11, 23), "勤労感謝の日"), holidays)
        self.assertEqual(
            holidays, [it.to_tuple() for it in JPHoliday().year_holidays(9999)]
        )

    def test_year_holidays_min(self):
        self.assertEqual(jpholiday.year_holidays(1), [])

    def test_month_holidays_max(self):
        self.assertEqual(
            jpholiday.month_holidays(9999, 11),
            [
                (datetime.date(9999, 11, 3), "文化の日"),
                (datetime.date(9999, 11, 23), "勤労感謝の日"),
            ],
        )
        self.assertEqual(jpholiday.month_holidays(9999, 12), [])

    def test_month_holidays_min(self):
        self.assertEqual(jpholiday.month_holidays(1, 1), [])

    def test_between_max(self):
        self.assertEqual(
            jpholiday.between(datetime.date(9999, 12, 1), datetime.date.max), []
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(9999, 12, 1), datetime.datetime.max), []
        )
        self.assertEqual(jpholiday.between(datetime.date.max, datetime.date.max), [])

    def test_between_min(self):
        self.assertEqual(
            jpholiday.between(datetime.date.min, datetime.date(1, 1, 31)), []
        )
        self.assertEqual(jpholiday.between(datetime.date.min, datetime.date.min), [])
