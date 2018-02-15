# -*- coding: utf-8 -*-

import datetime
import math
import calendar

def is_holiday_name(date):
	"""
	その日の祝日名を返します。
	"""
	if date < datetime.date(1948, 7, 20):
		return None
	else:
		name = None

	# 1月
	if date.month == 1:
		if date.day == 1:
			name = '元日'
		elif date.year <= 1999 and date.day == 15:
			name = '成人の日'
		elif date.year >= 2000 and date.day == _week_day(date, 2, 1).day:
			name = '成人の日'

	# 2月
	elif date.month == 2:
		if date.year >= 1967 and date.day == 11:
			name = '建国記念の日'

	# 3月
	elif date.month == 3:
		if date.day == _vernal_equinox_day(date.year):
			name = '春分の日'

	# 4月
	elif date.month == 4:
		if date.year <= 1988 and date.day == 29:
			name = '天皇誕生日'
		elif date.year >= 1989 and date.year <= 2006 and date.day == 29:
			name = 'みどりの日'
		elif date.year >= 2007 and date.day == 29:
			name = '昭和の日'

	# 5月
	elif date.month == 5:
		if date.day == 3:
			name = '憲法記念日'
		elif date.year >= 2007 and date.day == 4:
			name = 'みどりの日'
		elif date.day == 5:
			name = 'こどもの日'
		elif date.day == 6 and date.isoweekday() in (2, 3):
			holiday_name = _calc_date_holiday_name(date, datetime.timedelta(days=-date.isoweekday()))
			if holiday_name is not None:
				name = holiday_name+' 振替休日'

	# 7月
	elif date.month == 7:
		if date.year >= 1996 and date.year <= 2002 and date.day == 20:
			name = '海の日'
		elif date.year >= 2003 and date.day == _week_day(date, 3, 1).day:
			name = '海の日'

	# 8月
	elif date.month == 8:
		if date.year >= 2016 and date.day == 11:
			name = '山の日'

	# 9月
	elif date.month == 9:
		if date.year >= 1966 and date.year <= 2002 and date.day == 15:
			name = '敬老の日'
		elif date.year >= 2003 and date.day == _week_day(date, 3, 1).day:
			name = '敬老の日'
		elif _week_day(date, 3, 1).day == _autumn_equinox_day(date.year) -2 and date.day == (_week_day(date, 3, 1).day + 1):
			name = '国民の休日'
		elif date.day == _autumn_equinox_day(date.year):
			name = '秋分の日'

	# 10月
	elif date.month == 10:
		if date.year >= 1966 and date.year <= 1999 and date.day == 10:
			name = '体育の日'
		elif date.year >= 2003 and date.day == _week_day(date, 2, 1).day:
			name = '体育の日'

	# 11月
	elif date.month == 11:
		if date.day == 3:
			name = '文化の日'
		elif date.day == 23:
			name = '勤労感謝の日'

	# 12月
	elif date.month == 12:
		if date.day == 23:
			name = '天皇誕生日'

	# 皇室慶弔行事に伴う祝日
	if date == datetime.date(1959, 4, 10):
		name = '皇太子・明仁親王の結婚の儀'
	elif date == datetime.date(1989, 2, 24):
		name = '昭和天皇の大喪の礼'
	elif date == datetime.date(1990, 11, 12):
		name = '即位の礼正殿の儀'
	elif date == datetime.date(1993, 6, 9):
		name = '皇太子・皇太子徳仁親王の結婚の儀'

	# 振替休日
	if name is None and date.isoweekday() == 1:
		prev_name = _calc_date_holiday_name(date, datetime.timedelta(days=-1))
		if prev_name is not None:
			name = prev_name+' 振替休日'


	return name

def is_holiday(date):
	"""
	その日が祝日かどうかを返します。
	"""
	name = is_holiday_name(date)
	if name is None:
		return False

	return True

def year_holidays(year):
	"""
	その年の祝日日、祝日名を返します。
	"""
	date = datetime.date(year, 1, 1)

	output = []
	while date.year == year:
		name = is_holiday_name(date)
		if name is not None:
			output.append((date, name))

		date = date + datetime.timedelta(days=1)

	return output

def month_holidays(year, month):
	"""
	その月の祝日日、祝日名を返します。
	"""
	date = datetime.date(year, month, 1)

	output = []
	while date.month == month:
		name = is_holiday_name(date)
		if name is not None:
			output.append((date, name))

		date = date + datetime.timedelta(days=1)

	return output

def holidays(start_date, end_date):
	"""
	指定された期間の祝日日、祝日名を返します。
	"""
	output = []
	while start_date <= end_date:
		name = is_holiday_name(start_date)
		if name is not None:
			output.append((start_date, name))

		start_date = start_date + datetime.timedelta(days=1)

	return output

def _vernal_equinox_day(year):
	"""
	春季皇霊祭: 1879-1947
	春分の日: 1948
	春分の日の日付を返します。
	http://mt-soft.sakura.ne.jp/kyozai/excel_high/200_jissen_kiso/60_syunbun.htm
    """

	if year <= 1948:
		return 0

	if year >= 1851 and year <= 1899:
		i = 19.8277
	elif year >= 1900 and year <= 1979:
		i = 20.8357
	elif year >= 1980 and year <= 2099:
		i = 20.8431
	elif year >= 2100 and year <= 2150:
		i = 21.8510
	else:
		i = 0

	return math.floor(i + 0.242194 * (year - 1980) - math.floor((year - 1980) / 4))

def _autumn_equinox_day(year):
	"""
	秋分の日の日付を返します。
	秋季皇霊祭: 1879-1947
	秋分の日: 1948
	http://mt-soft.sakura.ne.jp/kyozai/excel_high/200_jissen_kiso/60_syunbun.htm
    """

	if year <= 1948:
		return 0

	if year >= 1851 and year <= 1899:
		i = 22.2588
	elif year >= 1900 and year <= 1979:
		i = 23.2588
	elif year >= 1980 and year <= 2099:
		i = 23.2488
	elif year >= 2100 and year <= 2150:
		i = 24.2488
	else:
		i = 0

	return math.floor(i + 0.242194 * (year - 1980) - math.floor((year - 1980) / 4))

def _calc_date_holiday_name(date, timedelta):
	"""
	日付計算後その日付の祝日名を返します。
    """
	old = date + timedelta
	old_name = is_holiday_name(old)
	return old_name

def _week_day(date, week, weekday):
	"""
	特定の月の第1月曜日などを返します。
    """
	if week < 1 or week > 5:
		return None

	if weekday < 1 or weekday > 7:
		return None

	lines = calendar.monthcalendar(date.year, date.month)

	days = []
	for line in lines:
		if line[weekday-1] == 0:
			continue

		days.append(line[weekday-1])

	return datetime.date(date.year, date.month, days[week-1])
