import datetime
from typing import Optional

from jpholiday.cache.interface import HolidayCacheInterface
from jpholiday.model.holiday import Holiday


class HolidayInMemoryCache(HolidayCacheInterface):
    def __init__(self) -> None:
        self._cache: dict[datetime.date, list[Holiday]] = {}

    def get(self, date: datetime.date) -> Optional[list[Holiday]]:
        return self._cache.get(date, None)

    def set(self, date: datetime.date, holidays: list[Holiday]) -> None:
        self._cache[date] = holidays

    def delete(self, date: datetime.date) -> None:
        self._cache.pop(date, None)

    def clear(self) -> None:
        self._cache.clear()
