# coding: utf-8
import unittest
import datetime
from jpholiday import jpholiday

class TestBasic(unittest.TestCase):

	# Init
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def test_vernal_equinox_day(self):
		"""
		春分の日
		"""
		self.assertEqual(jpholiday._vernal_equinox_day(2000), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2001), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2002), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2003), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2004), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2005), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2006), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2007), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2008), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2009), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2010), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2011), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2012), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2013), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2014), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2015), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2016), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2017), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2018), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2019), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2020), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2021), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2022), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2023), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2024), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2025), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2026), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2027), 21)
		self.assertEqual(jpholiday._vernal_equinox_day(2028), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2029), 20)
		self.assertEqual(jpholiday._vernal_equinox_day(2030), 20)

	def test_autumn_equinox_day(self):
		"""
		秋分の日
		"""
		self.assertEqual(jpholiday._autumn_equinox_day(2000), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2001), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2002), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2003), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2004), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2005), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2006), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2007), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2008), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2009), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2010), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2011), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2012), 22)
		self.assertEqual(jpholiday._autumn_equinox_day(2013), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2014), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2015), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2016), 22)
		self.assertEqual(jpholiday._autumn_equinox_day(2017), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2018), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2019), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2020), 22)
		self.assertEqual(jpholiday._autumn_equinox_day(2021), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2022), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2023), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2024), 22)
		self.assertEqual(jpholiday._autumn_equinox_day(2025), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2026), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2027), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2028), 22)
		self.assertEqual(jpholiday._autumn_equinox_day(2029), 23)
		self.assertEqual(jpholiday._autumn_equinox_day(2030), 23)

	def test_other_holiday(self):
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(1959, 4, 10)), '皇太子・明仁親王の結婚の儀')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(1989, 2, 24)), '昭和天皇の大喪の礼')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(1990, 11, 12)), '即位の礼正殿の儀')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(1993, 6, 9)), '皇太子・皇太子徳仁親王の結婚の儀')

	def test_2015(self):
		"""
		2015年祝日
		"""
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 1, 1)), '元日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 1, 12)), '成人の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 2, 11)), '建国記念の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 3, 21)), '春分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 4, 29)), '昭和の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 5, 3)), '憲法記念日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 5, 4)), 'みどりの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 5, 5)), 'こどもの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 5, 6)), '憲法記念日 振替休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 7, 20)), '海の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 9, 21)), '敬老の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 9, 22)), '国民の休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 9, 23)), '秋分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 10, 12)), '体育の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 11, 3)), '文化の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 11, 23)), '勤労感謝の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2015, 12, 23)), '天皇誕生日')

	def test_2015_month(self):
		"""
		2015年月祝日数
		"""
		self.assertEqual(len(jpholiday.month_holidays(2015, 1)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2015, 2)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2015, 3)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2015, 4)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2015, 5)), 4)
		self.assertEqual(len(jpholiday.month_holidays(2015, 6)), 0)
		self.assertEqual(len(jpholiday.month_holidays(2015, 7)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2015, 8)), 0)
		self.assertEqual(len(jpholiday.month_holidays(2015, 9)), 3)
		self.assertEqual(len(jpholiday.month_holidays(2015, 10)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2015, 11)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2015, 12)), 1)

	def test_2015_year(self):
		"""
		2015年祝日数
		"""
		self.assertEqual(len(jpholiday.year_holidays(2015)), 17)

	def test_2016(self):
		"""
		2016年祝日
		"""
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 1, 1)), '元日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 1, 11)), '成人の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 2, 11)), '建国記念の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 3, 20)), '春分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 3, 21)), '春分の日 振替休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 4, 29)), '昭和の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 5, 3)), '憲法記念日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 5, 4)), 'みどりの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 5, 5)), 'こどもの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 7, 18)), '海の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 8, 11)), '山の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 9, 19)), '敬老の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 9, 22)), '秋分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 10, 10)), '体育の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 11, 3)), '文化の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 11, 23)), '勤労感謝の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2016, 12, 23)), '天皇誕生日')
		self.assertEqual(len(jpholiday.year_holidays(2016)), 17)

	def test_2016_month(self):
		"""
		2016年月祝日数
		"""
		self.assertEqual(len(jpholiday.month_holidays(2016, 1)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2016, 2)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2016, 3)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2016, 4)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2016, 5)), 3)
		self.assertEqual(len(jpholiday.month_holidays(2016, 6)), 0)
		self.assertEqual(len(jpholiday.month_holidays(2016, 7)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2016, 8)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2016, 9)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2016, 10)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2016, 11)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2016, 12)), 1)

	def test_2016_year(self):
		"""
		2016年祝日数
		"""
		self.assertEqual(len(jpholiday.year_holidays(2016)), 17)


	def test_2017(self):
		"""
		2017年祝日
		"""
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 1, 1)), '元日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 1, 2)), '元日 振替休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 1, 9)), '成人の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 2, 11)), '建国記念の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 3, 20)), '春分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 4, 29)), '昭和の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 5, 3)), '憲法記念日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 5, 4)), 'みどりの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 5, 5)), 'こどもの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 7, 17)), '海の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 8, 11)), '山の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 9, 18)), '敬老の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 9, 23)), '秋分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 10, 9)), '体育の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 11, 3)), '文化の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 11, 23)), '勤労感謝の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2017, 12, 23)), '天皇誕生日')

	def test_2017_month(self):
		"""
		2017年月祝日数
		"""
		self.assertEqual(len(jpholiday.month_holidays(2017, 1)), 3)
		self.assertEqual(len(jpholiday.month_holidays(2017, 2)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2017, 3)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2017, 4)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2017, 5)), 3)
		self.assertEqual(len(jpholiday.month_holidays(2017, 6)), 0)
		self.assertEqual(len(jpholiday.month_holidays(2017, 7)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2017, 8)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2017, 9)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2017, 10)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2017, 11)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2017, 12)), 1)

	def test_2017_year(self):
		"""
		2017年祝日数
		"""
		self.assertEqual(len(jpholiday.year_holidays(2017)), 17)

	def test_2018(self):
		"""
		2018年祝日
		"""
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 1, 1)), '元日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 1, 8)), '成人の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 2, 11)), '建国記念の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 2, 12)), '建国記念の日 振替休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 3, 21)), '春分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 4, 29)), '昭和の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 4, 30)), '昭和の日 振替休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 5, 3)), '憲法記念日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 5, 4)), 'みどりの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 5, 5)), 'こどもの日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 7, 16)), '海の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 8, 11)), '山の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 9, 17)), '敬老の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 9, 23)), '秋分の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 9, 24)), '秋分の日 振替休日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 10, 8)), '体育の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 11, 3)), '文化の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 11, 23)), '勤労感謝の日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 12, 23)), '天皇誕生日')
		self.assertEqual(jpholiday.is_holiday_name(datetime.date(2018, 12, 24)), '天皇誕生日 振替休日')

	def test_2018_month(self):
		"""
		2018年月祝日数
		"""
		self.assertEqual(len(jpholiday.month_holidays(2018, 1)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2018, 2)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2018, 3)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2018, 4)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2018, 5)), 3)
		self.assertEqual(len(jpholiday.month_holidays(2018, 6)), 0)
		self.assertEqual(len(jpholiday.month_holidays(2018, 7)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2018, 8)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2018, 9)), 3)
		self.assertEqual(len(jpholiday.month_holidays(2018, 10)), 1)
		self.assertEqual(len(jpholiday.month_holidays(2018, 11)), 2)
		self.assertEqual(len(jpholiday.month_holidays(2018, 12)), 2)

	def test_2018_year(self):
		"""
		2018年祝日数
		"""
		self.assertEqual(len(jpholiday.year_holidays(2018)), 20)
