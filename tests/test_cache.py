import datetime
import unittest

from jpholiday import JPHoliday
from jpholiday.cache.in_memory import HolidayInMemoryCache
from jpholiday.model.holiday import Holiday


class TestCache(unittest.TestCase):
    def test_clear_returned_list(self):
        """
        戻り値のリストを変更してもキャッシュが壊れないこと(祝日)
        """
        jpholiday = JPHoliday()
        expected = [Holiday(date=datetime.date(2017, 1, 1), name="元日")]

        # 初回(キャッシュ生成時)の戻り値を変更
        jpholiday.holidays(datetime.date(2017, 1, 1)).clear()
        self.assertEqual(jpholiday.is_holiday(datetime.date(2017, 1, 1)), True)
        self.assertEqual(jpholiday.holidays(datetime.date(2017, 1, 1)), expected)

        # 2回目以降(キャッシュヒット時)の戻り値を変更
        jpholiday.holidays(datetime.date(2017, 1, 1)).clear()
        self.assertEqual(jpholiday.is_holiday(datetime.date(2017, 1, 1)), True)
        self.assertEqual(jpholiday.holidays(datetime.date(2017, 1, 1)), expected)

    def test_append_returned_list(self):
        """
        戻り値のリストを変更してもキャッシュが壊れないこと(平日)
        """
        jpholiday = JPHoliday()
        dummy = Holiday(date=datetime.date(2017, 1, 3), name="dummy")

        # 初回(キャッシュ生成時)の戻り値を変更
        jpholiday.holidays(datetime.date(2017, 1, 3)).append(dummy)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2017, 1, 3)), False)
        self.assertEqual(jpholiday.holidays(datetime.date(2017, 1, 3)), [])

        # 2回目以降(キャッシュヒット時)の戻り値を変更
        jpholiday.holidays(datetime.date(2017, 1, 3)).append(dummy)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2017, 1, 3)), False)
        self.assertEqual(jpholiday.holidays(datetime.date(2017, 1, 3)), [])


class TestHolidayInMemoryCache(unittest.TestCase):
    def setUp(self):
        self.cache = HolidayInMemoryCache()
        self.date = datetime.date(2024, 1, 1)
        self.holidays = [Holiday(date=self.date, name="元日")]

    def test_get_missing(self):
        self.assertIsNone(self.cache.get(self.date))

    def test_set_and_get(self):
        self.cache.set(self.date, self.holidays)
        self.assertEqual(self.cache.get(self.date), self.holidays)

    def test_delete(self):
        self.cache.set(self.date, self.holidays)
        self.cache.delete(self.date)
        self.assertIsNone(self.cache.get(self.date))
        # 存在しないキーの削除はエラーにならない
        self.cache.delete(self.date)

    def test_clear(self):
        self.cache.set(self.date, self.holidays)
        self.cache.clear()
        self.assertIsNone(self.cache.get(self.date))
