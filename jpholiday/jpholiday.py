# -*- coding: utf-8 -*-

import datetime

from . import registry
from . import holiday


def is_holiday_name(date):
    """
    その日の祝日名を返します。
    """
    for holiday in registry.RegistryHolder.get_registry():
        if holiday.is_holiday_name(date):
            return holiday.is_holiday_name(date)

    return None


def is_holiday(date):
    """
    その日が祝日かどうかを返します。
    """
    for holiday in registry.RegistryHolder.get_registry():
        if holiday.is_holiday(date):
            return True

    return False


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
