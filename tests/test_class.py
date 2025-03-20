import datetime
import unittest

from jpholiday import JPHoliday
from jpholiday.model.holiday import Holiday


class TestClass(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_main(self):
        jpholiday = JPHoliday()

        self.assertEqual(
            jpholiday.holidays(datetime.date(2020, 1, 1)),
            [
                Holiday(
                    date=datetime.date(2020, 1, 1),
                    name='元日',
                ),
            ]
        )
        self.assertEqual(jpholiday.holidays(datetime.date(2020, 2, 3)), [])
        self.assertEqual(jpholiday.is_holiday(datetime.date(2020, 2, 3)), False)
