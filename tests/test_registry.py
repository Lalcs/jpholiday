import datetime
import unittest

from jpholiday.checker.interface import OriginalHolidayCheckerInterface
from jpholiday.registry.registry import HolidayCheckerRegistry


class _TestHolidayChecker(OriginalHolidayCheckerInterface):
    def is_holiday(self, date: datetime.date) -> bool:
        return date == datetime.date(2024, 2, 5)

    def holiday_name(self, date: datetime.date) -> str:
        return "特別休暇"


class TestHolidayCheckerRegistry(unittest.TestCase):
    def test_register_same_type_only_once(self):
        registry = HolidayCheckerRegistry()
        count = len(registry.checkers())

        registry.register(_TestHolidayChecker())
        registry.register(_TestHolidayChecker())

        self.assertEqual(len(registry.checkers()), count + 1)
        self.assertEqual(
            sum(isinstance(c, _TestHolidayChecker) for c in registry.checkers()), 1
        )

    def test_unregister(self):
        registry = HolidayCheckerRegistry()
        count = len(registry.checkers())

        registry.register(_TestHolidayChecker())
        registry.unregister(_TestHolidayChecker())

        self.assertEqual(len(registry.checkers()), count)
        self.assertFalse(
            any(isinstance(c, _TestHolidayChecker) for c in registry.checkers())
        )
