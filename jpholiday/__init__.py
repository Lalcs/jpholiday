from .checker.interface import OriginalHolidayCheckerInterface
from .functions import *
from .jpholiday import JPHoliday

__all__ = [
    # クラス
    "JPHoliday",
    "OriginalHolidayCheckerInterface",
    # 関数
    "is_holiday",
    "is_holiday_name",
    "year_holidays",
    "month_holidays",
    "between",
    "register",
    "unregister",
    # バージョン
    "__version__",
]

"""
日本の祝日を扱うクラス
2016年 国民の祝日に関する法律の一部を改正する法律(平成26年法律第43号)
2019年 国民の祝日に関する法律の一部を改正する法律(昭和23年法律第178号)
2020年 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
2020年 国民の祝日に関する法律(昭和23年法律第178号)の特例
2019年 天皇の即位の日及び即位礼正殿の儀の行われる日を休日とする法律
2020年 五輪特別措置法改正案
"""

# Version will be dynamically set by poetry-dynamic-versioning
try:
    from ._version import __version__
except ImportError:
    # Fallback for development
    __version__ = '0.0.0'
