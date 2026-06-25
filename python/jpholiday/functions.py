import datetime
from typing import Optional, Union

from jpholiday.jpholiday import JPHoliday, OriginalHolidayCheckerInterface

new_api = JPHoliday()


def is_holiday_name(date: Union[datetime.date, datetime.datetime]) -> Optional[str]:
    """
    その日の祝日名を返します。
    """

    result = new_api.holidays(date)

    if len(result) == 0:
        return None

    return result[0].name


def is_holiday(date: Union[datetime.date, datetime.datetime]) -> bool:
    """
    その日が祝日かどうかを返します。
    """

    return new_api.is_holiday(date)


def year_holidays(year: int) -> list[tuple[datetime.date, str]]:
    """
    その年の祝日日、祝日名を返します。
    """

    result = new_api.year_holidays(year)
    return [it.to_tuple() for it in result]


def month_holidays(year: int, month: int) -> list[tuple[datetime.date, str]]:
    """
    その月の祝日日、祝日名を返します。
    """

    result = new_api.month_holidays(year, month)
    return [it.to_tuple() for it in result]


def between(
        start_date: Union[datetime.date, datetime.datetime],
        end_date: Union[datetime.date, datetime.datetime]
) -> list[tuple[datetime.date, str]]:
    """
    指定された期間の祝日日、祝日名を返します。
    """

    result = new_api.between(start_date, end_date)
    return [it.to_tuple() for it in result]


def register(checker: OriginalHolidayCheckerInterface) -> None:
    """
    独自の祝日チェッカーを登録します。
    """
    new_api.register(checker)


def unregister(checker: OriginalHolidayCheckerInterface) -> None:
    """
    独自の祝日チェッカーを登録解除します。
    """
    new_api.unregister(checker)
