# coding: utf-8
import datetime
import unittest

import jpholiday

class TestBasic(unittest.TestCase):

    # Init
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_original_holiday(self):
        """
        独自の休み
        """
        class TestHoliday(jpholiday.OriginalHoliday):
            def _is_holiday(self, date):
                if date == datetime.date(2020, 2, 3) or date == datetime.date(2020, 2, 5):
                    return True
                if date == datetime.date(2020, 2, 9):
                    return True
                return False

            def _is_holiday_name(self, date):
                return '特別休暇'

        # 国民の休日
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 3)), '特別休暇')
        self.assertEqual(jpholiday.is_holiday(datetime.date(2020, 2, 4)), False)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 5)), '特別休暇')

        # 振替休日
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 9)), '特別休暇')
        self.assertEqual(jpholiday.is_holiday(datetime.date(2020, 2, 10)), False)

        # 登録解除
        jpholiday.OriginalHoliday.unregister(TestHoliday)

        # 再登録
        jpholiday.OriginalHoliday.register(TestHoliday)

        # 国民の休日
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 3)), '特別休暇')
        self.assertEqual(jpholiday.is_holiday(datetime.date(2020, 2, 4)), False)
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 5)), '特別休暇')

        # 振替休日
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(2020, 2, 9)), '特別休暇')
        self.assertEqual(jpholiday.is_holiday(datetime.date(2020, 2, 10)), False)

        # 登録解除
        jpholiday.OriginalHoliday.unregister(TestHoliday)

    def test_vernal_equinox_day(self):
        """
        春分の日
        """
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2000), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2001), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2002), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2003), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2004), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2005), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2006), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2007), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2008), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2009), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2010), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2011), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2012), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2013), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2014), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2015), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2016), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2017), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2018), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2019), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2020), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2021), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2022), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2023), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2024), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2025), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2026), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2027), 21)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2028), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2029), 20)
        self.assertEqual(jpholiday.holiday.VernalEquinoxDay._vernal_equinox_day(2030), 20)

    def test_autumn_equinox_day(self):
        """
        秋分の日
        """
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2000), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2001), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2002), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2003), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2004), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2005), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2006), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2007), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2008), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2009), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2010), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2011), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2012), 22)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2013), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2014), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2015), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2016), 22)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2017), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2018), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2019), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2020), 22)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2021), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2022), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2023), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2024), 22)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2025), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2026), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2027), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2028), 22)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2029), 23)
        self.assertEqual(jpholiday.holiday.AutumnEquinoxDay._autumn_equinox_day(2030), 23)

    def test_other_holiday(self):
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1959, 4, 10)), '皇太子・明仁親王の結婚の儀')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 2, 24)), '昭和天皇の大喪の礼')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 11, 12)), '即位の礼正殿の儀')
        self.assertEqual(jpholiday.is_holiday_name(datetime.date(1993, 6, 9)), '皇太子・皇太子徳仁親王の結婚の儀')
