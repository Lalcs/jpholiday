import datetime

from jpholiday.cache.interface import HolidayCacheInterface
from jpholiday.model.holiday import Holiday


class HolidayInMemoryCache(HolidayCacheInterface):
    def __init__(self):
        self._cache: list[Holiday] = []

    def get(self, date: datetime.date) -> list[Holiday]:
        return [holiday for holiday in self._cache if holiday.date == date]

    def set(self, holiday: Holiday):
        self._cache.append(holiday)

    def delete(self, date: datetime.date):
        for it in self.get(date):
            self._cache.remove(it)
