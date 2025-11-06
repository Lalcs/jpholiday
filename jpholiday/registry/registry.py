from jpholiday.checker.checker import *
from jpholiday.checker.interface import HolidayCheckerInterface
from jpholiday.registry.interface import CheckerRegistryInterface


class HolidayCheckerRegistry(CheckerRegistryInterface):
    def __init__(self) -> None:
        self._checker: list[HolidayCheckerInterface] = [
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

    def register(self, checker: HolidayCheckerInterface) -> None:
        if any(isinstance(h, type(checker)) for h in self._checker):
            return
        self._checker.append(checker)

    def unregister(self, checker: HolidayCheckerInterface) -> None:
        self._checker = [h for h in self._checker if not isinstance(h, type(checker))]
