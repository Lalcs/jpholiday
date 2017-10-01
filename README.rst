JPHoliday
====================================================

日本の祝日を取得するライブラリ

Installation
-----------------

.. code-block:: bash

    $ pip install jpholiday

Sample Code
-----------------

.. code-block:: python

    # 指定日の祝日名を取得
    import jpholiday
    import datetime
    jpholiday.is_holiday_name(datetime.date(2017, 1, 1))
    > '元日'
    jpholiday.is_holiday_name(datetime.date(2017, 1, 2))
    > '元日 振替休日'
    jpholiday.is_holiday_name(datetime.date(2017, 1, 3))
    > None

    # 指定日が祝日か判定
    import jpholiday
    import datetime
    jpholiday.is_holiday(datetime.date(2017, 1, 1))
    > True
    jpholiday.is_holiday(datetime.date(2017, 1, 2))
    > True
    jpholiday.is_holiday(datetime.date(2017, 1, 3))
    > False

    # 指定年の祝日を取得
    import jpholiday
    jpholiday.year_holidays(2017)
    >[(datetime.date(2017, 1, 1), '元日'),
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

    # 指定月の祝日を取得
    import jpholiday
    jpholiday.month_holidays(2017, 5)
    >[(datetime.date(2017, 5, 3), '憲法記念日'),
     (datetime.date(2017, 5, 4), 'みどりの日'),
     (datetime.date(2017, 5, 5), 'こどもの日')]

    # 指定範囲の祝日を取得
    import jpholiday
    import datetime
    jpholiday.holidays(datetime.date(2017, 1, 1), datetime.date(2017, 5, 3))
    >[(datetime.date(2017, 1, 1), '元日'),
     (datetime.date(2017, 1, 2), '元日 振替休日'),
     (datetime.date(2017, 1, 9), '成人の日'),
     (datetime.date(2017, 2, 11), '建国記念の日'),
     (datetime.date(2017, 3, 20), '春分の日'),
     (datetime.date(2017, 4, 29), '昭和の日'),
     (datetime.date(2017, 5, 3), '憲法記念日')]
