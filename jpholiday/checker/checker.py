import datetime

from jpholiday.checker import utils
from jpholiday.checker import astronomy
from jpholiday.checker.interface import HolidayCheckerInterface, OriginalHolidayCheckerInterface
from jpholiday.registry.interface import CheckerRegistryInterface


# 元日
class NewYearChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.month == 1 and date.day == 1

    def holiday_name(self, date: datetime.date) -> str:
        return '元日'


# 成人の日
class AdultDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.year <= 1999 and date.month == 1 and date.day == 15:
            return True
        elif date.year >= 2000 and date.month == 1 and date.day == utils._week_day(date, 2, 1).day:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '成人の日'


# 建国記念の日
class FoundationDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.year >= 1967 and date.month == 2 and date.day == 11

    def holiday_name(self, date: datetime.date) -> str:
        return '建国記念の日'


# 天皇誕生日
class EmperorsBirthdayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.year in range(1948, 1988 + 1) and date.month == 4 and date.day == 29:
            return True
        elif date.year in range(1989, 2018 + 1) and date.month == 12 and date.day == 23:
            return True
        elif date.year >= 2020 and date.month == 2 and date.day == 23:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '天皇誕生日'


# 春分の日
class VernalEquinoxDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.month == 3 and date.day == self._vernal_equinox_day(date.year):
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '春分の日'

    @staticmethod
    def _vernal_equinox_day(year):
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
        if date.year in range(1989, 2006 + 1) and date.month == 4 and date.day == 29:
            return True
        elif date.year >= 2007 and date.month == 5 and date.day == 4:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return 'みどりの日'


# 昭和の日
class ShowaDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.year >= 2007 and date.month == 4 and date.day == 29:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '昭和の日'


# 憲法記念日
class ConstitutionMemorialDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.month == 5 and date.day == 3:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '憲法記念日'


# こどもの日
class ChildrensDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.month == 5 and date.day == 5:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return 'こどもの日'


# 海の日
class SeaDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            if date == datetime.date(2020, 7, 23):
                return True

            return False

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            if date == datetime.date(2021, 7, 22):
                return True

            return False

        if date.year in range(1996, 2002 + 1) and date.month == 7 and date.day == 20:
            return True
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        elif date.year >= 2003 and date.month == 7 and date.day == utils._week_day(date, 3,
                                                                                   1).day:
            return True

        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '海の日'


# 山の日
class MountainDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            if date == datetime.date(2020, 8, 10):
                return True

            return False

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            if date == datetime.date(2021, 8, 8):
                return True

            return False

        # 2016: 国民の祝日に関する法律の一部を改正する法律(平成26年法律第43号)
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        if date.year >= 2016 and date.month == 8 and date.day == 11:
            return True

        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '山の日'


# 敬老の日
class RespectForTheAgedDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.year in range(1966, 2002 + 1) and date.month == 9 and date.day == 15:
            return True
        elif date.year >= 2003 and date.month == 9 and date.day == utils._week_day(date, 3, 1).day:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '敬老の日'


# 秋分の日
class AutumnEquinoxDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.month == 9 and date.day == self._autumn_equinox_day(date.year):
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '秋分の日'

    @staticmethod
    def _autumn_equinox_day(year):
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
        if date.year in range(1966, 1999 + 1) and date.month == 10 and date.day == 10:
            return True
        elif date.year in range(2000, 2019 + 1) and date.month == 10 and date.day == utils._week_day(date, 2, 1).day:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '体育の日'


# スポーツの日
class SportsDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            if date == datetime.date(2020, 7, 24):
                return True

            return False

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            if date == datetime.date(2021, 7, 23):
                return True

            return False

        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        #       国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year >= 2020 and date.month == 10 and date.day == utils._week_day(date, 2, 1).day:
            return True

        return False

    def holiday_name(self, date: datetime.date) -> str:
        return 'スポーツの日'


# 文化の日
class CultureDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.month == 11 and date.day == 3:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '文化の日'


# 勤労感謝の日
class LaborThanksgivingDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        if date.month == 11 and date.day == 23:
            return True
        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '勤労感謝の日'


# 1959年 皇太子・明仁親王の結婚の儀
class ExtraHoliday1959Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1959, 4, 10)

    def holiday_name(self, date: datetime.date) -> str:
        return '皇太子・明仁親王の結婚の儀'


# 1989年 昭和天皇の大喪の礼
class ExtraHoliday1989Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1989, 2, 24)

    def holiday_name(self, date: datetime.date) -> str:
        return '昭和天皇の大喪の礼'


# 1990年 即位の礼正殿の儀
class ExtraHoliday1990Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1990, 11, 12)

    def holiday_name(self, date: datetime.date) -> str:
        return '即位の礼正殿の儀'


# 1993年 皇太子・皇太子徳仁親王の結婚の儀
class ExtraHoliday1993Checker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(1993, 6, 9)

    def holiday_name(self, date: datetime.date) -> str:
        return '皇太子・皇太子徳仁親王の結婚の儀'


# 2019年5月1日 天皇の即位の日
class ExtraHoliday2019MayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(2019, 5, 1)

    def holiday_name(self, date: datetime.date) -> str:
        return '天皇の即位の日'


# 2019年10月22日 即位礼正殿の儀
class ExtraHoliday2019OctChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(2019, 10, 22)

    def holiday_name(self, date: datetime.date) -> str:
        return '即位礼正殿の儀'


# 振替休日
class TransferHolidayChecker(HolidayCheckerInterface):

    def __init__(self, registry: CheckerRegistryInterface) -> None:
        self._registry = registry

    def is_holiday(self, date: datetime.date) -> bool:
        if self.__transfer_holiday_name(date) == "":
            return False
        return True

    def holiday_name(self, date: datetime.date) -> str:
        return self.__transfer_holiday_name(date)

    def __transfer_holiday_name(self, date: datetime.date) -> str:
        # 1973年(昭和48年)4月12日 - 改正・施行
        if date.year < 1973:
            return ""

        # 日曜日に振替休日は存在しない
        if date.isoweekday() == 7:
            return ""

        filtered_registry = list(
            filter(
                lambda x:
                not isinstance(x, TransferHolidayChecker)
                and not isinstance(x, NationalHolidayChecker)
                and not isinstance(x, OriginalHolidayCheckerInterface),
                self._registry.checkers()
            )
        )

        # 祝日が存在する日に振替休日は存在しない
        if len(list(filter(lambda x: x.is_holiday(date), filtered_registry))) != 0:
            return ""

        current_date = date - datetime.timedelta(days=1)

        while (True):
            current_registry = list(filter(lambda x: x.is_holiday(current_date), filtered_registry))
            if len(current_registry) == 0:
                return ""

            if current_date.isoweekday() == 7:
                if len(current_registry) != 0:
                    return '{} {}'.format(
                        current_registry[0].holiday_name(current_date),
                        '振替休日'
                    )
                else:
                    return ""

            current_date = current_date - datetime.timedelta(days=1)


# 国民の休日
class NationalHolidayChecker(HolidayCheckerInterface):
    def __init__(self, registry: CheckerRegistryInterface) -> None:
        self._registry = registry

    def is_holiday(self, date: datetime.date) -> bool:

        if date.isoweekday() == 7:
            return False

        filtered_registry = list(
            filter(
                lambda x:
                not isinstance(x, NationalHolidayChecker)
                and not isinstance(x, OriginalHolidayCheckerInterface),
                self._registry.checkers()
            )
        )

        if len(list(filter(lambda x: x.is_holiday(date), filtered_registry))) != 0:
            return False

        if (
                len(list(filter(lambda x: x.is_holiday(date + datetime.timedelta(days=1)), filtered_registry))) != 0
                and len(list(filter(lambda x: x.is_holiday(date - datetime.timedelta(days=1)), filtered_registry))) != 0
        ):
            return True

        return False

    def holiday_name(self, date: datetime.date) -> str:
        return '国民の休日'
