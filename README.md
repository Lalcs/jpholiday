# JPHoliday

[![image](https://img.shields.io/pypi/v/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/pypi/l/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/pypi/pyversions/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/github/contributors/lalcs/jpholiday.svg)](https://github.com/lalcs/jpholiday/graphs/contributors)
[![image](https://img.shields.io/pypi/dm/jpholiday)](https://pypistats.org/packages/jpholiday)
![Unittest](https://github.com/Lalcs/jpholiday/workflows/Unittest/badge.svg)

日本の祝日を取得するライブラリ

## Installation

```bash
pip install jpholiday
```

## Sample Code

### 指定日の祝日名を取得

```python
import jpholiday
import datetime

# datetime.date
jpholiday.is_holiday_name(datetime.date(2017, 1, 1))
> '元日'
jpholiday.is_holiday_name(datetime.date(2017, 1, 2))
> '元日 振替休日'
jpholiday.is_holiday_name(datetime.date(2017, 1, 3))
> None

# datetime.datetime
jpholiday.is_holiday_name(datetime.datetime(2017, 1, 1, 1, 1, 1))
> '元日'
jpholiday.is_holiday_name(datetime.datetime(2017, 1, 2, 1, 1, 1))
> '元日 振替休日'
jpholiday.is_holiday_name(datetime.datetime(2017, 1, 3, 1, 1, 1))
> None
```

### 指定日が祝日か判定

```python
import jpholiday
import datetime

# datetime.date
jpholiday.is_holiday(datetime.date(2017, 1, 1))
> True
jpholiday.is_holiday(datetime.date(2017, 1, 2))
> True
jpholiday.is_holiday(datetime.date(2017, 1, 3))
> False

# datetime.datetime
jpholiday.is_holiday(datetime.datetime(2017, 1, 1, 1, 1, 1))
> True
jpholiday.is_holiday(datetime.datetime(2017, 1, 2, 1, 1, 1))
> True
jpholiday.is_holiday(datetime.datetime(2017, 1, 3, 1, 1, 1))
> False
```

### 指定年の祝日を取得

```python
import jpholiday

jpholiday.year_holidays(2017)
> [(datetime.date(2017, 1, 1), '元日'),
   (datetime.date(2017, 1, 2), '元日 振替休日'),
   (datetime.date(2017, 1, 9), '成人の日'),
   (datetime.date(2017, 2, 11), '建国記念の日'),
   (datetime.date(2017, 3, 20), '春分の日'),
   (datetime.date(2017, 4, 29), '昭和の日'),
   (datetime.date(2017, 5, 3), '憲法記念日'),
   (datetime.date(2017, 5, 4), 'みどりの日'),
   (datetime.date(2017, 5, 5), 'こどもの日'),
   (datetime.date(2017, 7, 17), '海の日'),
   (datetime.date(2017, 8, 11), '山の日'),
   (datetime.date(2017, 9, 18), '敬老の日'),
   (datetime.date(2017, 9, 23), '秋分の日'),
   (datetime.date(2017, 10, 9), '体育の日'),
   (datetime.date(2017, 11, 3), '文化の日'),
   (datetime.date(2017, 11, 23), '勤労感謝の日'),
   (datetime.date(2017, 12, 23), '天皇誕生日')]
```

### 指定月の祝日を取得

```python
import jpholiday

jpholiday.month_holidays(2017, 5)
> [(datetime.date(2017, 5, 3), '憲法記念日'),
   (datetime.date(2017, 5, 4), 'みどりの日'),
   (datetime.date(2017, 5, 5), 'こどもの日')]
```

### 指定範囲の祝日を取得

```python
import jpholiday
import datetime

# datetime.date
jpholiday.between(datetime.date(2017, 1, 1), datetime.date(2017, 5, 3))
> [(datetime.date(2017, 1, 1), '元日'),
   (datetime.date(2017, 1, 2), '元日 振替休日'),
   (datetime.date(2017, 1, 9), '成人の日'),
   (datetime.date(2017, 2, 11), '建国記念の日'),
   (datetime.date(2017, 3, 20), '春分の日'),
   (datetime.date(2017, 4, 29), '昭和の日'),
   (datetime.date(2017, 5, 3), '憲法記念日')]

# datetime.datetime
jpholiday.between(datetime.datetime(2017, 1, 1, 3, 15, 0), datetime.datetime(2017, 5, 3, 12, 30, 12))
> [(datetime.date(2017, 1, 1), '元日'),
   (datetime.date(2017, 1, 2), '元日 振替休日'),
   (datetime.date(2017, 1, 9), '成人の日'),
   (datetime.date(2017, 2, 11), '建国記念の日'),
   (datetime.date(2017, 3, 20), '春分の日'),
   (datetime.date(2017, 4, 29), '昭和の日'),
   (datetime.date(2017, 5, 3), '憲法記念日')]
```

### 独自の休日を追加

```python
import jpholiday
import datetime


class TestHoliday(jpholiday.OriginalHoliday):
    def _is_holiday(self, date):
        if date == datetime.date(2020, 2, 9):
            return True
        return False

    def _is_holiday_name(self, date):
        return '特別休暇'


jpholiday.is_holiday_name(datetime.date(2020, 2, 9))
> '特別休暇'

jpholiday.is_holiday(datetime.date(2020, 2, 9))
> True
```

### 独自の休日を削除

```python
import jpholiday

jpholiday.OriginalHoliday.unregister(TestHoliday)
```

## Example

### 独自の休日をファイルから読み込む

```python
import jpholiday
import configparser


class TestHoliday(jpholiday.OriginalHoliday):
    original_holidays = {}

    config = configparser.ConfigParser()
    config.read('holidays.ini')
    if 'HOLIDAYS' in config:
        original_holidays = config['HOLIDAYS']

    def _is_holiday(self, date):
        if date in [datetime.strptime(holiday, '%Y-%m-%d').date() for holiday in self.original_holidays.keys()]:
            return True
        return False

    def _is_holiday_name(self, date):
        if date.strftime('%Y-%m-%d') in self.original_holidays.keys():
            return self.original_holidays[date.strftime('%Y-%m-%d')]
        else:
            return None


'holidays.ini'
[HOLIDAYS]
2021 - 02 - 22: 特別休暇1
2021 - 02 - 24: 特別休暇2

jpholiday.is_holiday(datetime.date(2021, 2, 22))
> True

jpholiday.is_holiday_name(datetime.date(2021, 2, 22))
> 特別休暇1
```

## Star History

<a href="https://www.star-history.com/#Lalcs/jpholiday&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Lalcs/jpholiday&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Lalcs/jpholiday&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Lalcs/jpholiday&type=Date" />
 </picture>
</a>