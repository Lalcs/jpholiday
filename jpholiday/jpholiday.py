import datetime
from typing import Any, Union

from jpholiday.cache.in_memory import HolidayInMemoryCache
from jpholiday.checker.interface import OriginalHolidayCheckerInterface
from jpholiday.exception import JPHolidayTypeError
from jpholiday.model.holiday import Holiday
from jpholiday.registy.registry import HolidayCheckerRegistry


class JPHoliday:
    def __init__(self):
        self._cache = HolidayInMemoryCache()
        self.registry = HolidayCheckerRegistry()

    def holidays(self, date: Union[datetime.date, datetime.datetime]) -> list[Holiday]:
        """
        その日の祝日名を返します。
        """

        date = self._to_date(date)

        cache = self._cache.get(date)
        if cache is not None:
            return cache

        holidays = []
        for holiday in self.registry.checkers():
            if holiday.is_holiday(date):
                holidays.append(Holiday(date, holiday.holiday_name(date)))

        self._cache.set(date, holidays)

        return holidays

    def is_holiday(self, date: Union[datetime.date, datetime.datetime]) -> bool:
        """
        その日が祝日かどうかを返します。
        """

        date = self._to_date(date)

        if len(self.holidays(date)) != 0:
            return True

        return False

    def year_holidays(self, year: int) -> list[Holiday]:
        """
        その年の祝日日、祝日名を返します。
        """
        date = datetime.date(year, 1, 1)

        holidays = []
        while date.year == year:
            result = self.holidays(date)
            if len(result) != 0:
                holidays.extend(result)

            date = date + datetime.timedelta(days=1)

        return holidays

    def month_holidays(self, year: int, month: int) -> list[Holiday]:
        """
        その月の祝日日、祝日名を返します。
        """
        date = datetime.date(year, month, 1)

        holidays = []
        while date.month == month:
            result = self.holidays(date)
            if len(result) != 0:
                holidays.extend(result)

            date = date + datetime.timedelta(days=1)

        return holidays

    def between(self, start_date: datetime.date, end_date: datetime.date) -> list[Holiday]:
        """
        指定された期間の祝日日、祝日名を返します。
        """

        current_date = self._to_date(start_date)
        end_date = self._to_date(end_date)

        holidays = []
        while current_date <= end_date:
            result = self.holidays(current_date)
            if len(result) != 0:
                holidays.extend(result)

            current_date = current_date + datetime.timedelta(days=1)

        return holidays

    def _to_date(self, value: Any) -> datetime.date:
        """
        datetime型をdate型へ変換
        それ以外は例外
        """
        if isinstance(value, datetime.datetime):
            return value.date()
        if isinstance(value, datetime.date):
            return value
        raise JPHolidayTypeError("is type datetime or date isinstance only.")

    def register(self, checker: OriginalHolidayCheckerInterface):
        """
        独自の祝日チェッカーを登録します。
        """
        self._cache.clear()
        self.registry.register(checker)

    def unregister(self, checker: OriginalHolidayCheckerInterface):
        """
        独自の祝日チェッカーを登録解除します。
        """
        self._cache.clear()
        self.registry.unregister(checker)
