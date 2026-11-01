import datetime
import unittest

from jpholiday.cache.in_memory import HolidayInMemoryCache
from jpholiday.model.holiday import Holiday


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
