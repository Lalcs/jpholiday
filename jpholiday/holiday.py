# -*- coding: utf-8 -*-

import datetime
import math

from . import registry
from . import utils


# 元日
class NewYear(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 1 and date.day == 1:
            return True
        return False

    def _is_holiday_name(self, date):
        return '元日'


# 成人の日
class AdultDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year <= 1999 and date.month == 1 and date.day == 15:
            return True
        elif date.year >= 2000 and date.month == 1 and date.day == utils._week_day(date, 2, 1).day:
            return True
        return False

    def _is_holiday_name(self, date):
        return '成人の日'


# 建国記念の日
class FoundationDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year >= 1967 and date.month == 2 and date.day == 11:
            return True
        return False

    def _is_holiday_name(self, date):
        return '建国記念の日'


# 天皇誕生日
class EmperorsBirthday(registry.BaseHoliday):
    def _is_holiday(self, date):
        # 1948-1988年
        if date.year in range(1948, 1988 + 1) and date.month == 4 and date.day == 29:
            return True
        # 1988-2018年
        # 2019: 国民の祝日に関する法律(昭和23年法律第178号)の一部改正
        elif date.year in range(1988, 2018 + 1) and date.month == 12 and date.day == 23:
            return True
        # 2019: 国民の祝日に関する法律(昭和23年法律第178号)の一部改正
        elif date.year >= 2020 and date.month == 2 and date.day == 23:
            return True
        return False

    def _is_holiday_name(self, date):
        return '天皇誕生日'


# 春分の日
class VernalEquinoxDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 3 and date.day == self._vernal_equinox_day(date.year):
            return True
        return False

    def _is_holiday_name(self, date):
        return '春分の日'

    @staticmethod
    def _vernal_equinox_day(year):
        """
        春季皇霊祭: 1879-1947
        春分の日: 1948
        春分の日の日付を返します。
        http://mt-soft.sakura.ne.jp/kyozai/excel_high/200_jissen_kiso/60_syunbun.htm
        """

        if year <= 1948:
            return 0

        if year >= 1851 and year <= 1899:
            i = 19.8277
        elif year >= 1900 and year <= 1979:
            i = 20.8357
        elif year >= 1980 and year <= 2099:
            i = 20.8431
        elif year >= 2100 and year <= 2150:
            i = 21.8510
        else:
            i = 0

        return math.floor(i + 0.242194 * (year - 1980) - math.floor((year - 1980) / 4))


# みどりの日
class GreeneryDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year >= 1989 and date.year <= 2006 and date.month == 4 and date.day == 29:
            return True
        elif date.year >= 2007 and date.month == 5 and date.day == 4:
            return True
        return False

    def _is_holiday_name(self, date):
        return 'みどりの日'


# 昭和の日
class ShowaDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year >= 2007 and date.month == 4 and date.day == 29:
            return True
        return False

    def _is_holiday_name(self, date):
        return '昭和の日'


# 憲法記念日
class ConstitutionMemorialDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 5 and date.day == 3:
            return True
        return False

    def _is_holiday_name(self, date):
        return '憲法記念日'


# こどもの日
class ChildrensDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 5 and date.day == 5:
            return True
        return False

    def _is_holiday_name(self, date):
        return 'こどもの日'


# 海の日
class SeaDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year >= 1996 and date.month == 7 and date.year <= 2002 and date.day == 20:
            return True
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        elif date.year >= 2003 and date.month == 7 and date.year != 2020 and date.day == utils._week_day(date, 3,
                                                                                                         1).day:
            return True

        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date == datetime.date(2020, 7, 23):
            return True

        return False

    def _is_holiday_name(self, date):
        return '海の日'


# 山の日
class MountainDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        # 2016: 国民の祝日に関する法律の一部を改正する法律(平成26年法律第43号)
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        if date.year >= 2016 and date.year != 2020 and date.month == 8 and date.day == 11:
            return True

        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date == datetime.date(2020, 8, 10):
            return True

        return False

    def _is_holiday_name(self, date):
        return '山の日'


# 敬老の日
class RespectForTheAgedDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year >= 1966 and date.year <= 2002 and date.month == 9 and date.day == 15:
            return True
        elif date.year >= 2003 and date.month == 9 and date.day == utils._week_day(date, 3, 1).day:
            return True
        return False

    def _is_holiday_name(self, date):
        return '敬老の日'


# 秋分の日
class AutumnEquinoxDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 9 and date.day == self._autumn_equinox_day(date.year):
            return True
        return False

    def _is_holiday_name(self, date):
        return '秋分の日'

    @staticmethod
    def _autumn_equinox_day(year):
        """
        秋分の日の日付を返します。
        秋季皇霊祭: 1879-1947
        秋分の日: 1948
        http://mt-soft.sakura.ne.jp/kyozai/excel_high/200_jissen_kiso/60_syunbun.htm
        """

        if year <= 1948:
            return 0

        if year >= 1851 and year <= 1899:
            i = 22.2588
        elif year >= 1900 and year <= 1979:
            i = 23.2588
        elif year >= 1980 and year <= 2099:
            i = 23.2488
        elif year >= 2100 and year <= 2150:
            i = 24.2488
        else:
            i = 0

        return math.floor(i + 0.242194 * (year - 1980) - math.floor((year - 1980) / 4))


# 体育の日
class HealthAndSportsDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.year >= 1966 and date.year <= 1999 and date.month == 10 and date.day == 10:
            return True
        elif date.year >= 2000 and date.year <= 2019 and date.month == 10 and date.day == utils._week_day(date, 2,
                                                                                                          1).day:
            return True
        return False

    def _is_holiday_name(self, date):
        return '体育の日'


# スポーツの日
class SportsDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        #       国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year >= 2020 and date.year != 2020 and date.month == 10 and date.day == utils._week_day(date, 2, 1).day:
            return True

        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date == datetime.date(2020, 7, 24):
            return True

        return False

    def _is_holiday_name(self, date):
        return 'スポーツの日'


# 文化の日
class CultureDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 11 and date.day == 3:
            return True
        return False

    def _is_holiday_name(self, date):
        return '文化の日'


# 勤労感謝の日
class LaborThanksgivingDay(registry.BaseHoliday):
    def _is_holiday(self, date):
        if date.month == 11 and date.day == 23:
            return True
        return False

    def _is_holiday_name(self, date):
        return '勤労感謝の日'


# 皇室慶弔行事に伴う祝日
class ExtraHolidays(registry.BaseHoliday):
    def _is_holiday(self, date):
        if self.__extra_holiday_name(date) is None:
            return False
        return True

    def _is_holiday_name(self, date):
        return self.__extra_holiday_name(date)

    def __extra_holiday_name(self, date):
        if date == datetime.date(1959, 4, 10):
            return '皇太子・明仁親王の結婚の儀'
        elif date == datetime.date(1989, 2, 24):
            return '昭和天皇の大喪の礼'
        elif date == datetime.date(1990, 11, 12):
            return '即位の礼正殿の儀'
        elif date == datetime.date(1993, 6, 9):
            return '皇太子・皇太子徳仁親王の結婚の儀'
        elif date == datetime.date(2019, 5, 1):
            return '天皇の即位の日'
        # 2019: 天皇の即位の日及び即位礼正殿の儀の行われる日を休日とする法律
        elif date == datetime.date(2019, 10, 22):
            return '即位礼正殿の儀'
        return None


# 振替休日
class TransferHoliday(registry.BaseHoliday):

    def _is_holiday(self, date):
        if self.__transfer_holiday_name(date) is None:
            return False
        return True

    def _is_holiday_name(self, date):
        return self.__transfer_holiday_name(date)

    def __transfer_holiday_name(self, date):
        # 1973年(昭和48年)4月12日 - 改正・施行
        if date.year < 1973:
            return None

        # GW
        if date.month == 5 and date.day == 6 and date.isoweekday() in (2, 3):
            for holiday in registry.RegistryHolder.get_registry():
                if holiday.__class__.__name__ == self.__class__.__name__:
                    continue

                if isinstance(holiday, NationalHoliday):
                    continue

                if isinstance(holiday, registry.OriginalHoliday):
                    continue

                if holiday.is_holiday((date + datetime.timedelta(days=-date.isoweekday()))):
                    return '{} {}'.format(
                        holiday.is_holiday_name((date + datetime.timedelta(days=-date.isoweekday()))),
                        '振替休日')

        # 月曜日でない
        if date.isoweekday() != 1:
            return None

        # GW以外
        for holiday in registry.RegistryHolder.get_registry():
            if holiday.__class__.__name__ == self.__class__.__name__:
                continue

            if isinstance(holiday, NationalHoliday):
                continue

            if isinstance(holiday, registry.OriginalHoliday):
                continue

            if holiday.is_holiday((date + datetime.timedelta(days=-1))):
                return '{} {}'.format(holiday.is_holiday_name((date + datetime.timedelta(days=-1))),
                                      '振替休日')


# 国民の休日
class NationalHoliday(registry.BaseHoliday):
    def _is_holiday(self, date):

        result = {
            'old': False,
            'new': False,
        }

        for holiday in registry.RegistryHolder.get_registry():
            if holiday.__class__.__name__ == self.__class__.__name__:
                continue

            if isinstance(holiday, registry.OriginalHoliday):
                continue

            if holiday.is_holiday((date + datetime.timedelta(days=-1))):
                result['old'] = True
            if holiday.is_holiday((date + datetime.timedelta(days=1))):
                result['new'] = True

            if list(result.values()) == [True, True]:
                return True

        return False

    def _is_holiday_name(self, date):
        return '国民の休日'
