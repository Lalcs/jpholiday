import datetime
import unittest

import jpholiday
from jpholiday.exception import JPHolidayTypeError


class TestException(unittest.TestCase):

    def test_is_holiday_name(self):
        """
        型チェック
        """
        with self.assertRaises(JPHolidayTypeError):
            jpholiday.is_holiday_name(21210101)

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.is_holiday_name('2021-01-01')

    def test_is_holiday(self):
        """
        型チェック
        """
        with self.assertRaises(JPHolidayTypeError):
            jpholiday.is_holiday(21210101)

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.is_holiday('2021-01-01')

    def test_between(self):
        """
        型チェック
        """
        with self.assertRaises(JPHolidayTypeError):
            jpholiday.between(21210101, 20210101)

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.between(datetime.date(2021, 1, 1), 20210101)

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.between(20210101, datetime.date(2021, 1, 1))

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.between('2021-01-01', '2021-01-01')

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.between(datetime.date(2021, 1, 1), '2021-01-01')

        with self.assertRaises(JPHolidayTypeError):
            jpholiday.between('2021-01-01', datetime.date(2021, 1, 1))
