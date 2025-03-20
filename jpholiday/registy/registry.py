from jpholiday.checker.checker import *
from jpholiday.checker.interface import HolidayCheckerInterface
from jpholiday.registy.interface import CheckerRegistryInterface


class HolidayCheckerRegistry(CheckerRegistryInterface):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def __init__(self):
        self._checker = [
            NewYearChecker(),
            AdultDayChecker(),
            FoundationDayChecker(),
            EmperorsBirthdayChecker(),
            VernalEquinoxDayChecker(),
            GreeneryDayChecker(),
            ShowaDayChecker(),
            ConstitutionMemorialDayChecker(),
            ChildrensDayChecker(),
            SeaDayChecker(),
            MountainDayChecker(),
            RespectForTheAgedDayChecker(),
            AutumnEquinoxDayChecker(),
            HealthAndSportsDayChecker(),
            SportsDayChecker(),
            CultureDayChecker(),
            LaborThanksgivingDayChecker(),
            ExtraHoliday1959Checker(),
            ExtraHoliday1989Checker(),
            ExtraHoliday1990Checker(),
            ExtraHoliday1993Checker(),
            ExtraHoliday2019MayChecker(),
            ExtraHoliday2019OctChecker(),
            TransferHolidayChecker(self),
            NationalHolidayChecker(self),
        ]

    def checkers(self) -> list[HolidayCheckerInterface]:
        return self._checker

    def register(self, checker: HolidayCheckerInterface):
        if any(isinstance(h, type(checker)) for h in self._checker):
            return
        self._checker.append(checker)

    def unregister(self, checker: HolidayCheckerInterface):
        self._checker = [h for h in self._checker if not isinstance(h, type(checker))]
