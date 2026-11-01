import calendar
import datetime
from collections.abc import Iterator
from typing import Any

from jpholiday.cache.in_memory import HolidayInMemoryCache
from jpholiday.checker.interface import OriginalHolidayCheckerInterface
from jpholiday.exception import JPHolidayTypeError
from jpholiday.model.holiday import Holiday
from jpholiday.registry.registry import HolidayCheckerRegistry


class JPHoliday:
    def __init__(self) -> None:
        self._cache = HolidayInMemoryCache()
        self.registry = HolidayCheckerRegistry()

    def holidays(self, date: datetime.date | datetime.datetime) -> list[Holiday]:
        """
        その日の祝日名を返します。
        """

        date = self._to_date(date)

        # 戻り値はキャッシュ本体とは別のリストにする。
        # 呼び出し側が戻り値を変更してもキャッシュが壊れないようにするため。
        cache = self._cache.get(date)
        if cache is not None:
            return list(cache)

        holidays = []
        for holiday in self.registry.checkers():
            if holiday.is_holiday(date):
                holidays.append(Holiday(date, holiday.holiday_name(date)))

        self._cache.set(date, holidays)

        return list(holidays)

    def is_holiday(self, date: datetime.date | datetime.datetime) -> bool:
        """
        その日が祝日かどうかを返します。
        """

        date = self._to_date(date)

        return len(self.holidays(date)) != 0

    def year_holidays(self, year: int) -> list[Holiday]:
        """
        その年の祝日日、祝日名を返します。
        """
        return list(self.iter_year_holidays(year))

    def iter_year_holidays(self, year: int) -> Iterator[Holiday]:
        """
        指定された年の祝日日、祝日名をイテレーターで返します。
        """
        yield from self.iter_between(
            datetime.date(year, 1, 1), datetime.date(year, 12, 31)
        )

    def month_holidays(self, year: int, month: int) -> list[Holiday]:
        """
        その月の祝日日、祝日名を返します。
        """
        return list(self.iter_month_holidays(year, month))

    def iter_month_holidays(self, year: int, month: int) -> Iterator[Holiday]:
        """
        指定された月の祝日日、祝日名をイテレーターで返します。
        """
        first_date = datetime.date(year, month, 1)
        last_date = first_date.replace(day=calendar.monthrange(year, month)[1])

        yield from self.iter_between(first_date, last_date)

    def between(
        self,
        start_date: datetime.date | datetime.datetime,
        end_date: datetime.date | datetime.datetime,
    ) -> list[Holiday]:
        """
        指定された期間の祝日日、祝日名をリストで返します。
        """
        return list(self.iter_between(start_date, end_date))

    def iter_between(
        self,
        start_date: datetime.date | datetime.datetime,
        end_date: datetime.date | datetime.datetime,
    ) -> Iterator[Holiday]:
        """
        指定された期間の祝日日、祝日名をイテレーターで返します。
        """
        start_date = self._to_date(start_date)
        end_date = self._to_date(end_date)

        # 日付の通し番号で回すことで、end_date が datetime.date.max の場合でも
        # 翌日の計算による OverflowError を起こさない
        for ordinal in range(start_date.toordinal(), end_date.toordinal() + 1):
            yield from self.holidays(datetime.date.fromordinal(ordinal))

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
