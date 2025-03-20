from abc import abstractmethod, ABC

from jpholiday.checker.interface import HolidayCheckerInterface


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
