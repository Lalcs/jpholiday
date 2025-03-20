import datetime
from abc import abstractmethod, ABC


class HolidayCheckerInterface(ABC):
    @abstractmethod
    def is_holiday(self, date: datetime.date) -> bool:
        pass

    @abstractmethod
    def holiday_name(self, date: datetime.date) -> str:
        pass


class OriginalHolidayCheckerInterface(HolidayCheckerInterface, ABC):
    pass


class CheckerRegistryInterface(ABC):
    @abstractmethod
    def checkers(self) -> list[HolidayCheckerInterface]:
        pass

    @abstractmethod
    def register(self, checker: HolidayCheckerInterface):
        pass

    @abstractmethod
    def unregister(self, checker: HolidayCheckerInterface):
        pass
