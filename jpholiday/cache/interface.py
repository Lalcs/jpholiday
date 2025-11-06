import datetime
from abc import ABC, abstractmethod
from typing import Optional

from jpholiday.model.holiday import Holiday


class HolidayCacheInterface(ABC):
    @abstractmethod
    def get(self, date: datetime.date) -> Optional[list[Holiday]]:
        pass

    @abstractmethod
    def set(self, date: datetime.date, holidays: list[Holiday]) -> None:
        pass

    @abstractmethod
    def delete(self, date: datetime.date) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
