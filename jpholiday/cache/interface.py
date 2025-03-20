import datetime
from abc import ABC, abstractmethod

from jpholiday.model.holiday import Holiday


class HolidayCacheInterface(ABC):
    @abstractmethod
    def get(self, date: datetime.date) -> list[Holiday]:
        pass

    @abstractmethod
    def set(self, holiday: Holiday):
        pass

    @abstractmethod
    def delete(self, date: datetime.date):
        pass
