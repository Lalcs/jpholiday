import calendar
import datetime
from typing import Optional


def _week_day(date: datetime.date, week: int, weekday: int) -> Optional[datetime.date]:
    """
    特定の月の第1月曜日などを返します。
    """
    if week < 1 or week > 5:
        return None

    if weekday < 1 or weekday > 7:
        return None

    c = calendar.TextCalendar(firstweekday=calendar.MONDAY)
    lines = c.monthdayscalendar(date.year, date.month)

    days = []
    for line in lines:
        if line[weekday - 1] == 0:
            continue

        days.append(line[weekday - 1])

    return datetime.date(date.year, date.month, days[week - 1])
