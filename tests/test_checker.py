import datetime
import unittest

from jpholiday.checker import utils
from jpholiday.checker.checker import (
    AutumnEquinoxDayChecker,
    VernalEquinoxDayChecker,
    _is_nth_weekday,
)


class TestWeekDay(unittest.TestCase):
    def test_week_day(self):
        # 2024年1月の第2月曜日は8日
        self.assertEqual(
            utils._week_day(datetime.date(2024, 1, 1), 2, 1),
            datetime.date(2024, 1, 8),
        )
        # 2024年9月の第3月曜日は16日 (1日が日曜日の月)
        self.assertEqual(
            utils._week_day(datetime.date(2024, 9, 30), 3, 1),
            datetime.date(2024, 9, 16),
        )

    def test_week_day_out_of_range(self):
        date = datetime.date(2024, 1, 1)
        self.assertIsNone(utils._week_day(date, 0, 1))
        self.assertIsNone(utils._week_day(date, 6, 1))
        self.assertIsNone(utils._week_day(date, 1, 0))
        self.assertIsNone(utils._week_day(date, 1, 8))

    def test_is_nth_weekday(self):
        self.assertTrue(_is_nth_weekday(datetime.date(2024, 1, 8), 2, 1))
        self.assertFalse(_is_nth_weekday(datetime.date(2024, 1, 15), 2, 1))

    def test_is_nth_weekday_out_of_range(self):
        self.assertFalse(_is_nth_weekday(datetime.date(2024, 1, 8), 0, 1))
        self.assertFalse(_is_nth_weekday(datetime.date(2024, 1, 8), 2, 8))


class TestEquinoxDayBefore1948(unittest.TestCase):
    def test_vernal_equinox_day(self):
        self.assertEqual(VernalEquinoxDayChecker._vernal_equinox_day(1947), 0)
        self.assertEqual(VernalEquinoxDayChecker._vernal_equinox_day(1948), 21)

    def test_autumn_equinox_day(self):
        self.assertEqual(AutumnEquinoxDayChecker._autumn_equinox_day(1947), 0)
        self.assertEqual(AutumnEquinoxDayChecker._autumn_equinox_day(1948), 23)
        # 国民の祝日に関する法律の施行前のため、秋分の日は存在しない
        self.assertFalse(
            AutumnEquinoxDayChecker().is_holiday(datetime.date(1947, 9, 23))
        )
