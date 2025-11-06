import datetime
from typing import Any, Union, Iterator

from jpholiday.cache.in_memory import HolidayInMemoryCache
from jpholiday.checker.interface import OriginalHolidayCheckerInterface
from jpholiday.exception import JPHolidayTypeError
from jpholiday.model.holiday import Holiday
from jpholiday.registry.registry import HolidayCheckerRegistry


class JPHoliday:
    def __init__(self) -> None:
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
        return list(self.iter_year_holidays(year))

    def iter_year_holidays(self, year: int) -> Iterator[Holiday]:
        """
        指定された年の祝日日、祝日名をイテレーターで返します。
        """
        date = datetime.date(year, 1, 1)

        while date.year == year:
            result = self.holidays(date)
            if result:
                for holiday in result:
                    yield holiday

            date = date + datetime.timedelta(days=1)

    def month_holidays(self, year: int, month: int) -> list[Holiday]:
        """
        その月の祝日日、祝日名を返します。
        """
        return list(self.iter_month_holidays(year, month))

    def iter_month_holidays(self, year: int, month: int) -> Iterator[Holiday]:
        """
        指定された月の祝日日、祝日名をイテレーターで返します。
        """
        date = datetime.date(year, month, 1)

        while date.month == month:
            result = self.holidays(date)
            if result:
                for holiday in result:
                    yield holiday

            date = date + datetime.timedelta(days=1)

    def between(
            self,
            start_date: Union[datetime.date, datetime.datetime],
            end_date: Union[datetime.date, datetime.datetime]
    ) -> list[Holiday]:
        """
        指定された期間の祝日日、祝日名をリストで返します。
        """
        return list(self.iter_between(start_date, end_date))

    def iter_between(
            self,
            start_date: Union[datetime.date, datetime.datetime],
            end_date: Union[datetime.date, datetime.datetime]
    ) -> Iterator[Holiday]:
        """
        指定された期間の祝日日、祝日名をイテレーターで返します。
        """
        current_date = self._to_date(start_date)
        end_date = self._to_date(end_date)

        while current_date <= end_date:
            result = self.holidays(current_date)
            if result:
                for holiday in result:
                    yield holiday

            current_date = current_date + datetime.timedelta(days=1)

    def _to_date(self, value: Any) -> datetime.date:
        """
        datetime型をdate型へ変換
        それ以外は例外
        """
        if isinstance(value, datetime.datetime):
            return value.date()
        if isinstance(value, datetime.date):
            return value
        raise JPHolidayTypeError(
            f"Expected datetime.date or datetime.datetime, got {type(value).__name__}"
        )

    def register(self, checker: OriginalHolidayCheckerInterface) -> None:
        """
        独自の祝日チェッカーを登録します。
        """
        self._cache.clear()
        self.registry.register(checker)

    def unregister(self, checker: OriginalHolidayCheckerInterface) -> None:
        """
        独自の祝日チェッカーを登録解除します。
        """
        self._cache.clear()
        self.registry.unregister(checker)
