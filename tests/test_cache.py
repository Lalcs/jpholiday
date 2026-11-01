import datetime
import unittest

from jpholiday import JPHoliday
from jpholiday.model.holiday import Holiday


class TestCache(unittest.TestCase):

    def test_clear_returned_list(self):
        """
        戻り値のリストを変更してもキャッシュが壊れないこと(祝日)
        """
        jpholiday = JPHoliday()
        expected = [Holiday(date=datetime.date(2017, 1, 1), name='元日')]

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
        dummy = Holiday(date=datetime.date(2017, 1, 3), name='dummy')

        # 初回(キャッシュ生成時)の戻り値を変更
        jpholiday.holidays(datetime.date(2017, 1, 3)).append(dummy)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2017, 1, 3)), False)
        self.assertEqual(jpholiday.holidays(datetime.date(2017, 1, 3)), [])

        # 2回目以降(キャッシュヒット時)の戻り値を変更
        jpholiday.holidays(datetime.date(2017, 1, 3)).append(dummy)
        self.assertEqual(jpholiday.is_holiday(datetime.date(2017, 1, 3)), False)
        self.assertEqual(jpholiday.holidays(datetime.date(2017, 1, 3)), [])
