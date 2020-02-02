# -*- coding: utf-8 -*-
import calendar
import datetime


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
        if line[weekday - 1] == 0:
            continue

        days.append(line[weekday - 1])

    return datetime.date(date.year, date.month, days[week - 1])
