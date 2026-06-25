"""春分・秋分チェッカーの互換シム。

組込み祝日の判定は Rust エンジンが行うため、これらのクラスは実際の祝日判定では使用されない。
`VernalEquinoxDayChecker._vernal_equinox_day` / `AutumnEquinoxDayChecker._autumn_equinox_day` を
直接参照する既存の白箱テストとの後方互換のために残している。計算はすべて Rust 製の天文関数
（`jpholiday.checker.astronomy`）へ委譲する。
"""
import datetime

from jpholiday.checker import astronomy
from jpholiday.checker.interface import HolidayCheckerInterface


# 春分の日
class VernalEquinoxDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.month == 3 and date.day == self._vernal_equinox_day(date.year)

    def holiday_name(self, date: datetime.date) -> str:
        return '春分の日'

    @staticmethod
    def _vernal_equinox_day(year: int) -> int:
        return astronomy.calculate_vernal_equinox(year)


# 秋分の日
class AutumnEquinoxDayChecker(HolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date.month == 9 and date.day == self._autumn_equinox_day(date.year)

    def holiday_name(self, date: datetime.date) -> str:
        return '秋分の日'

    @staticmethod
    def _autumn_equinox_day(year: int) -> int:
        return astronomy.calculate_autumn_equinox(year)
