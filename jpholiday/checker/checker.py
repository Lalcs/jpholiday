import datetime

from jpholiday.checker import astronomy, utils
from jpholiday.checker.interface import (
    HolidayCheckerInterface,
    OriginalHolidayCheckerInterface,
)
from jpholiday.registry.interface import CheckerRegistryInterface

# 1948年(昭和23年)7月20日 - 国民の祝日に関する法律(昭和23年法律第178号) 公布・施行
_HOLIDAY_ACT_ENFORCEMENT_DATE = datetime.date(1948, 7, 20)


def _is_nth_weekday(date: datetime.date, week: int, weekday: int) -> bool:
    """
    指定日がその月の第 week 週の weekday 曜日(1: 月曜日 〜 7: 日曜日)かどうかを返します。
    """
    nth_weekday = utils._week_day(date, week, weekday)
    return nth_weekday is not None and date.day == nth_weekday.day


# 元日
class NewYearChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return date.month == 1 and date.day == 1

    def holiday_name(self, date: datetime.date) -> str:
        return "元日"


# 成人の日
class AdultDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return (date.year <= 1999 and date.month == 1 and date.day == 15) or (
            date.year >= 2000 and date.month == 1 and _is_nth_weekday(date, 2, 1)
        )

    def holiday_name(self, date: datetime.date) -> str:
        return "成人の日"


# 建国記念の日
class FoundationDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.year >= 1967 and date.month == 2 and date.day == 11

    def holiday_name(self, date: datetime.date) -> str:
        return "建国記念の日"


# 天皇誕生日
class EmperorsBirthdayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return (
            (date.year in range(1948, 1988 + 1) and date.month == 4 and date.day == 29)
            or (
                date.year in range(1989, 2018 + 1)
                and date.month == 12
                and date.day == 23
            )
            or (date.year >= 2020 and date.month == 2 and date.day == 23)
        )

    def holiday_name(self, date: datetime.date) -> str:
        return "天皇誕生日"


# 春分の日
class VernalEquinoxDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return date.month == 3 and date.day == self._vernal_equinox_day(date.year)

    def holiday_name(self, date: datetime.date) -> str:
        return "春分の日"

    @staticmethod
    def _vernal_equinox_day(year: int) -> int:
        """
        春季皇霊祭: 1879-1947
        春分の日: 1948-
        春分の日の日付を返します。

        Uses astronomical calculations based on the Sun's ecliptic longitude.
        The spring equinox occurs when the Sun's ecliptic longitude is 0°.

        Accuracy: ±1 day
        Supported range: 1948-3000+
        Dependencies: Standard library only
        """

        if year < 1948:
            return 0

        return astronomy.calculate_vernal_equinox(year)


# みどりの日
class GreeneryDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return (
            date.year in range(1989, 2006 + 1) and date.month == 4 and date.day == 29
        ) or (date.year >= 2007 and date.month == 5 and date.day == 4)

    def holiday_name(self, date: datetime.date) -> str:
        return "みどりの日"


# 昭和の日
class ShowaDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.year >= 2007 and date.month == 4 and date.day == 29

    def holiday_name(self, date: datetime.date) -> str:
        return "昭和の日"


# 憲法記念日
class ConstitutionMemorialDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return date.month == 5 and date.day == 3

    def holiday_name(self, date: datetime.date) -> str:
        return "憲法記念日"


# こどもの日
class ChildrensDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return date.month == 5 and date.day == 5

    def holiday_name(self, date: datetime.date) -> str:
        return "こどもの日"


# 海の日
class SeaDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            return date == datetime.date(2020, 7, 23)

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            return date == datetime.date(2021, 7, 22)

        return (
            (date.year in range(1996, 2002 + 1) and date.month == 7 and date.day == 20)
            # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
            or (date.year >= 2003 and date.month == 7 and _is_nth_weekday(date, 3, 1))
        )

    def holiday_name(self, date: datetime.date) -> str:
        return "海の日"


# 山の日
class MountainDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            return date == datetime.date(2020, 8, 10)

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            return date == datetime.date(2021, 8, 8)

        # 2016: 国民の祝日に関する法律の一部を改正する法律(平成26年法律第43号)
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        return date.year >= 2016 and date.month == 8 and date.day == 11

    def holiday_name(self, date: datetime.date) -> str:
        return "山の日"


# 敬老の日
class RespectForTheAgedDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return (
            date.year in range(1966, 2002 + 1) and date.month == 9 and date.day == 15
        ) or (date.year >= 2003 and date.month == 9 and _is_nth_weekday(date, 3, 1))

    def holiday_name(self, date: datetime.date) -> str:
        return "敬老の日"


# 秋分の日
class AutumnEquinoxDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.month == 9 and date.day == self._autumn_equinox_day(date.year)

    def holiday_name(self, date: datetime.date) -> str:
        return "秋分の日"

    @staticmethod
    def _autumn_equinox_day(year: int) -> int:
        """
        秋季皇霊祭: 1879-1947
        秋分の日: 1948-
        秋分の日の日付を返します。

        Uses astronomical calculations based on the Sun's ecliptic longitude.
        The autumn equinox occurs when the Sun's ecliptic longitude is 180°.

        Accuracy: ±1 day
        Supported range: 1948-3000+
        Dependencies: Standard library only
        """

        if year < 1948:
            return 0

        return astronomy.calculate_autumn_equinox(year)


# 体育の日
class HealthAndSportsDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return (
            date.year in range(1966, 1999 + 1) and date.month == 10 and date.day == 10
        ) or (
            date.year in range(2000, 2019 + 1)
            and date.month == 10
            and _is_nth_weekday(date, 2, 1)
        )

    def holiday_name(self, date: datetime.date) -> str:
        return "体育の日"


# スポーツの日
class SportsDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            return date == datetime.date(2020, 7, 24)

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            return date == datetime.date(2021, 7, 23)

        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        #       国民の祝日に関する法律(昭和23年法律第178号)の特例
        return date.year >= 2020 and date.month == 10 and _is_nth_weekday(date, 2, 1)

    def holiday_name(self, date: datetime.date) -> str:
        return "スポーツの日"


# 文化の日
class CultureDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return date.month == 11 and date.day == 3

    def holiday_name(self, date: datetime.date) -> str:
        return "文化の日"


# 勤労感謝の日
class LaborThanksgivingDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date < _HOLIDAY_ACT_ENFORCEMENT_DATE:
            return False
        return date.month == 11 and date.day == 23

    def holiday_name(self, date: datetime.date) -> str:
        return "勤労感謝の日"


# 1959年 皇太子・明仁親王の結婚の儀
class ExtraHoliday1959Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1959, 4, 10)

    def holiday_name(self, date: datetime.date) -> str:
        return "皇太子・明仁親王の結婚の儀"


# 1989年 昭和天皇の大喪の礼
class ExtraHoliday1989Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1989, 2, 24)

    def holiday_name(self, date: datetime.date) -> str:
        return "昭和天皇の大喪の礼"


# 1990年 即位の礼正殿の儀
class ExtraHoliday1990Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1990, 11, 12)

    def holiday_name(self, date: datetime.date) -> str:
        return "即位の礼正殿の儀"


# 1993年 皇太子・皇太子徳仁親王の結婚の儀
class ExtraHoliday1993Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1993, 6, 9)

    def holiday_name(self, date: datetime.date) -> str:
        return "皇太子・皇太子徳仁親王の結婚の儀"


# 2019年5月1日 天皇の即位の日
class ExtraHoliday2019MayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(2019, 5, 1)

    def holiday_name(self, date: datetime.date) -> str:
        return "天皇の即位の日"


# 2019年10月22日 即位礼正殿の儀
class ExtraHoliday2019OctChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(2019, 10, 22)

    def holiday_name(self, date: datetime.date) -> str:
        return "即位礼正殿の儀"


# 振替休日
class TransferHolidayChecker(HolidayCheckerInterface):
    def __init__(self, registry: CheckerRegistryInterface) -> None:
        self._registry = registry

    def is_holiday(self, date: datetime.date) -> bool:
        return self.__transfer_holiday_name(date) != ""

    def holiday_name(self, date: datetime.date) -> str:
        return self.__transfer_holiday_name(date)

    def __transfer_holiday_name(self, date: datetime.date) -> str:
        # 1973年(昭和48年)4月12日 - 改正・施行
        if date < datetime.date(1973, 4, 12):
            return ""

        # 日曜日に振替休日は存在しない
        if date.isoweekday() == 7:
            return ""

        filtered_registry = list(
            filter(
                lambda x: (
                    not isinstance(x, TransferHolidayChecker)
                    and not isinstance(x, NationalHolidayChecker)
                    and not isinstance(x, OriginalHolidayCheckerInterface)
                ),
                self._registry.checkers(),
            )
        )

        # 祝日が存在する日に振替休日は存在しない
        if len(list(filter(lambda x: x.is_holiday(date), filtered_registry))) != 0:
            return ""

        current_date = date - datetime.timedelta(days=1)

        while True:
            current_registry = list(
                filter(lambda x: x.is_holiday(current_date), filtered_registry)
            )
            if len(current_registry) == 0:
                return ""

            if current_date.isoweekday() == 7:
                if len(current_registry) != 0:
                    return "{} {}".format(
                        current_registry[0].holiday_name(current_date), "振替休日"
                    )
                else:
                    return ""

            current_date = current_date - datetime.timedelta(days=1)


# 国民の休日
class NationalHolidayChecker(HolidayCheckerInterface):
    def __init__(self, registry: CheckerRegistryInterface) -> None:
        self._registry = registry

    def is_holiday(self, date: datetime.date) -> bool:
        # 1985年(昭和60年)12月27日 - 改正・施行
        if date < datetime.date(1985, 12, 27):
            return False

        if date.isoweekday() == 7:
            return False

        # 翌日が存在しない日(datetime.date.max)は「前日及び翌日が祝日」になり得ない
        if date == datetime.date.max:
            return False

        filtered_registry = list(
            filter(
                lambda x: (
                    not isinstance(x, NationalHolidayChecker)
                    and not isinstance(x, OriginalHolidayCheckerInterface)
                ),
                self._registry.checkers(),
            )
        )

        if len(list(filter(lambda x: x.is_holiday(date), filtered_registry))) != 0:
            return False

        return (
            len(
                list(
                    filter(
                        lambda x: x.is_holiday(date + datetime.timedelta(days=1)),
                        filtered_registry,
                    )
                )
            )
            != 0
            and len(
                list(
                    filter(
                        lambda x: x.is_holiday(date - datetime.timedelta(days=1)),
                        filtered_registry,
                    )
                )
            )
            != 0
        )

    def holiday_name(self, date: datetime.date) -> str:
        return "国民の休日"
