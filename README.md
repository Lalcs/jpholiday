# JPHoliday

[![image](https://img.shields.io/pypi/v/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/pypi/l/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/pypi/pyversions/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/github/contributors/lalcs/jpholiday.svg)](https://github.com/lalcs/jpholiday/graphs/contributors)
[![image](https://img.shields.io/pypi/dm/jpholiday)](https://pypistats.org/packages/jpholiday)
![Unittest](https://github.com/Lalcs/jpholiday/workflows/Unittest/badge.svg)

![image](./docs/images/logo.png)

このライブラリは、[内閣府](https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html)
が公表しているデータを基に、日本の国民の祝日を簡単に取得できるようにしたものです。  
**2026年**までの祝日は公式発表された内容に基づいて動作確認済みです。  
それ以降についても取得は可能ですが、内閣府からの正式な公表がないため、正確性は保証されません。

## Installation

```bash
pip install jpholiday
```

## Class

### 指定日の祝日名を取得

```python
from jpholiday import JPHoliday
import datetime

jpholiday = JPHoliday()

jpholiday.holidays(datetime.date(2017, 1, 1))
> [
    Holiday(
        date=datetime.date(2017, 1, 1),
        name='元日'
    )
]
jpholiday.holidays(datetime.date(2017, 1, 2))
> [
    Holiday(
        date=datetime.date(2017, 1, 2),
        name='元日 振替休日'
    )
]
jpholiday.holidays(datetime.date(2017, 1, 3))
> []
```

### 指定日が祝日か判定

```python
from jpholiday import JPHoliday
import datetime

jpholiday = JPHoliday()

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
from jpholiday import JPHoliday
import datetime

jpholiday = JPHoliday()

jpholiday.year_holidays(2017)
> [
    Holiday(
        date=datetime.date(2017, 1, 1),
        name='元日'
    ),
    Holiday(
        date=datetime.date(2017, 1, 2),
        name='元日 振替休日'
    ),
    ...
]
```

### 指定月の祝日を取得

```python
from jpholiday import JPHoliday
import datetime

jpholiday = JPHoliday()

jpholiday.month_holidays(2017, 5)
> [
    Holiday(
        date=datetime.date(2017, 5, 3),
        name='憲法記念日'
    ),
    Holiday(
        date=datetime.date(2017, 5, 4),
        name='みどりの日'
    ),
    Holiday(
        date=datetime.date(2017, 5, 5),
        name='こどもの日'
    )
]
```

### 指定範囲の祝日を取得

```python
from jpholiday import JPHoliday
import datetime

jpholiday = JPHoliday()

# datetime.date
jpholiday.between(datetime.date(2017, 1, 1), datetime.date(2017, 5, 3))
> [
    Holiday(
        date=datetime.date(2017, 1, 1),
        name='元日'
    ),
    Holiday(
        date=datetime.date(2017, 1, 2),
        name='元日 振替休日'
    ),
    ...
]

# datetime.datetime
jpholiday.between(datetime.datetime(2017, 1, 1, 3, 15, 0), datetime.datetime(2017, 5, 3, 12, 30, 12))
> [
    Holiday(
        date=datetime.date(2017, 1, 1),
        name='元日'
    ),
    Holiday(
        date=datetime.date(2017, 1, 2),
        name='元日 振替休日'
    ),
    ...
]
```

### 独自の休日を追加

```python
from jpholiday import JPHoliday, OriginalHolidayCheckerInterface
import datetime

jpholiday = JPHoliday()


class TestHoliday(OriginalHolidayCheckerInterface):
    def is_holiday(self, date):
        if date == datetime.date(2020, 2, 9):
            return True
        return False

    def holiday_name(self, date):
        return '特別休暇'


jpholiday.register(TestHoliday())

jpholiday.holidays(datetime.date(2020, 2, 9))
> [
    Holiday(
        date=datetime.date(2020, 2, 9),
        name='特別休暇'
    )
]

jpholiday.is_holiday(datetime.date(2020, 2, 9))
> True
```

### 独自の休日を削除

```python
from jpholiday import JPHoliday, OriginalHolidayCheckerInterface
import datetime

jpholiday = JPHoliday()


class TestHoliday(OriginalHolidayCheckerInterface):
    def is_holiday(self, date):
        if date == datetime.date(2020, 2, 9):
            return True
        return False

    def holiday_name(self, date):
        return '特別休暇'


jpholiday.unregister(TestHoliday())

jpholiday.holidays(datetime.date(2020, 2, 9))
> []

jpholiday.is_holiday(datetime.date(2020, 2, 9))
> False
```

## Functions

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


class TestHoliday(jpholiday.OriginalHolidayCheckerInterface):
    def is_holiday(self, date):
        if date == datetime.date(2020, 2, 9):
            return True
        return False

    def holiday_name(self, date):
        return '特別休暇'


jpholiday.register(TestHoliday())

jpholiday.is_holiday_name(datetime.date(2020, 2, 9))
> '特別休暇'

jpholiday.is_holiday(datetime.date(2020, 2, 9))
> True
```

### 独自の休日を削除

```python
import jpholiday
import datetime


class TestHoliday(jpholiday.OriginalHolidayCheckerInterface):
    def is_holiday(self, date):
        if date == datetime.date(2020, 2, 9):
            return True
        return False

    def holiday_name(self, date):
        return '特別休暇'


jpholiday.unregister(TestHoliday())

jpholiday.is_holiday_name(datetime.date(2020, 2, 9))
> None

jpholiday.is_holiday(datetime.date(2020, 2, 9))
> False
```
