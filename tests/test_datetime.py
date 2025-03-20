import datetime
import unittest

import jpholiday


class TestDateTime(unittest.TestCase):

    def test_datetime_sea_day(self):
        """
        海の日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2020, 7, 23, 1, 1, 1)), '海の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2021, 7, 22, 1, 1, 1)), '海の日')
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(2020, 7, 23, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(2021, 7, 22, 1, 1, 1)))
        self.assertEqual(
            jpholiday.between(datetime.datetime(2020, 7, 23, 1, 1, 1), datetime.datetime(2020, 7, 23, 1, 1, 1)),
            [(datetime.date(2020, 7, 23), '海の日')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(2021, 7, 22, 1, 1, 1), datetime.datetime(2021, 7, 22, 1, 1, 1)),
            [(datetime.date(2021, 7, 22), '海の日')]
        )

    def test_datetime_mountain_day(self):
        """
        山の日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2020, 8, 10, 1, 1, 1)), '山の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2021, 8, 8, 1, 1, 1)), '山の日')
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(2020, 8, 10, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(2021, 8, 8, 1, 1, 1)))
        self.assertEqual(
            jpholiday.between(datetime.datetime(2020, 8, 10, 1, 1, 1), datetime.datetime(2020, 8, 10, 1, 1, 1)),
            [(datetime.date(2020, 8, 10), '山の日')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(2021, 8, 8, 1, 1, 1), datetime.datetime(2021, 8, 8, 1, 1, 1)),
            [(datetime.date(2021, 8, 8), '山の日')]
        )

    def test_datetime_sports_day(self):
        """
        スポーツの日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2020, 7, 24, 1, 1, 1)), 'スポーツの日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2021, 7, 23, 1, 1, 1)), 'スポーツの日')
        self.assertTrue(jpholiday.is_holiday_name(datetime.datetime(2020, 7, 24, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday_name(datetime.datetime(2021, 7, 23, 1, 1, 1)))
        self.assertEqual(
            jpholiday.between(datetime.datetime(2020, 7, 24, 1, 1, 1), datetime.datetime(2020, 7, 24, 1, 1, 1)),
            [(datetime.date(2020, 7, 24), 'スポーツの日')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(2021, 7, 23, 1, 1, 1), datetime.datetime(2021, 7, 23, 1, 1, 1)),
            [(datetime.date(2021, 7, 23), 'スポーツの日')]
        )

    def test_datetime_other_holiday(self):
        """
        皇室慶弔行事に伴う祝日
        """
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(1959, 4, 10, 1, 1, 1)),
                         '皇太子・明仁親王の結婚の儀')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(1989, 2, 24, 1, 1, 1)), '昭和天皇の大喪の礼')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(1990, 11, 12, 1, 1, 1)), '即位の礼正殿の儀')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(1993, 6, 9, 1, 1, 1)),
                         '皇太子・皇太子徳仁親王の結婚の儀')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2019, 5, 1, 1, 1, 1)), '天皇の即位の日')
        self.assertEqual(jpholiday.is_holiday_name(datetime.datetime(2019, 10, 22, 1, 1, 1)), '即位礼正殿の儀')
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(1959, 4, 10, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(1989, 2, 24, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(1990, 11, 12, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(1993, 6, 9, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(2019, 5, 1, 1, 1, 1)))
        self.assertTrue(jpholiday.is_holiday(datetime.datetime(2019, 10, 22, 1, 1, 1)))
        self.assertEqual(
            jpholiday.between(datetime.datetime(1959, 4, 10, 1, 1, 1), datetime.datetime(1959, 4, 10, 1, 1, 1)),
            [(datetime.date(1959, 4, 10), '皇太子・明仁親王の結婚の儀')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(1989, 2, 24, 1, 1, 1), datetime.datetime(1989, 2, 24, 1, 1, 1)),
            [(datetime.date(1989, 2, 24), '昭和天皇の大喪の礼')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(1990, 11, 12, 1, 1, 1), datetime.datetime(1990, 11, 12, 1, 1, 1)),
            [(datetime.date(1990, 11, 12), '即位の礼正殿の儀')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(1993, 6, 9, 1, 1, 1), datetime.datetime(1993, 6, 9, 1, 1, 1)),
            [(datetime.date(1993, 6, 9), '皇太子・皇太子徳仁親王の結婚の儀')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(2019, 5, 1, 1, 1, 1), datetime.datetime(2019, 5, 1, 1, 1, 1)),
            [(datetime.date(2019, 5, 1), '天皇の即位の日')]
        )
        self.assertEqual(
            jpholiday.between(datetime.datetime(2019, 10, 22, 1, 1, 1), datetime.datetime(2019, 10, 22, 1, 1, 1)),
            [(datetime.date(2019, 10, 22), '即位礼正殿の儀')]
        )
