"""
Test cases for astronomical calculations module.

Tests cover:
- Accuracy of equinox calculations
- Performance requirements (< 1ms per calculation)
- Extended year range (1948-3000)
- Individual astronomical functions
"""

import time
import unittest
import math

from jpholiday.checker import astronomy


class TestAstronomicalCalculations(unittest.TestCase):
    """Test suite for astronomical calculation functions."""

    def test_julian_day_epoch_j2000(self):
        """Test Julian Day calculation for J2000.0 epoch."""
        # J2000.0 = 2000-01-01 12:00:00 UTC
        jd = astronomy.julian_day(2000, 1, 1, 12.0)
        self.assertAlmostEqual(jd, 2451545.0, places=5)

    def test_julian_day_various_dates(self):
        """Test Julian Day calculation for various known dates."""
        # Known test cases from Jean Meeus
        test_cases = [
            # (year, month, day, hour, expected_jd)
            (2000, 1, 1, 12.0, 2451545.0),
            (1999, 1, 1, 0.0, 2451179.5),
            (1987, 1, 27, 0.0, 2446822.5),
            (1988, 1, 27, 0.0, 2447187.5),  # Leap year
        ]

        for year, month, day, hour, expected_jd in test_cases:
            with self.subTest(date=f"{year}-{month:02d}-{day:02d}"):
                jd = astronomy.julian_day(year, month, day, hour)
                self.assertAlmostEqual(jd, expected_jd, places=4)

    def test_julian_day_to_datetime_epoch_j2000(self):
        """Test conversion from Julian Day back to datetime."""
        jd = 2451545.0
        dt = astronomy.julian_day_to_datetime(jd)
        self.assertEqual(dt.year, 2000)
        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 12)

    def test_normalize_angle(self):
        """Test angle normalization to [0, 360) range."""
        test_cases = [
            (0, 0),
            (360, 0),
            (720, 0),
            (-90, 270),
            (450, 90),
            (359.9, 359.9),
        ]

        for input_angle, expected in test_cases:
            with self.subTest(angle=input_angle):
                result = astronomy.normalize_angle(input_angle)
                self.assertAlmostEqual(result, expected, places=5)

    def test_solar_ecliptic_longitude_range(self):
        """Test that solar ecliptic longitude is always in [0, 360) range."""
        test_dates = [
            (2000, 1, 1),
            (2000, 3, 20),
            (2000, 6, 21),
            (2000, 9, 22),
            (2000, 12, 21),
        ]

        for year, month, day in test_dates:
            with self.subTest(date=f"{year}-{month:02d}-{day:02d}"):
                jd = astronomy.julian_day(year, month, day, 12.0)
                lon = astronomy.solar_ecliptic_longitude(jd)
                self.assertGreaterEqual(lon, 0.0)
                self.assertLess(lon, 360.0)

    def test_solar_ecliptic_longitude_approximate_values(self):
        """Test solar ecliptic longitude for approximate equinox/solstice dates."""
        test_cases = [
            # (year, month, day, expected_longitude, tolerance)
            (2000, 3, 20, 0.0, 5.0),     # Spring equinox ~0°
            (2000, 6, 21, 90.0, 5.0),    # Summer solstice ~90°
            (2000, 9, 22, 180.0, 5.0),   # Autumn equinox ~180°
            (2000, 12, 21, 270.0, 5.0),  # Winter solstice ~270°
        ]

        for year, month, day, expected_lon, tolerance in test_cases:
            with self.subTest(date=f"{year}-{month:02d}-{day:02d}"):
                jd = astronomy.julian_day(year, month, day, 12.0)
                lon = astronomy.solar_ecliptic_longitude(jd)

                # Handle wraparound at 0/360
                diff = abs(lon - expected_lon)
                if diff > 180:
                    diff = 360 - diff

                self.assertLess(diff, tolerance,
                               f"Longitude {lon}° not within {tolerance}° of {expected_lon}°")

    def test_vernal_equinox_historical_dates(self):
        """Test vernal equinox dates against historical records."""
        # Known vernal equinox dates from Japanese astronomical almanac
        known_equinoxes = [
            (1980, 20),
            (1990, 21),
            (2000, 20),
            (2010, 21),
            (2020, 20),
            (2024, 20),
            (2025, 20),
        ]

        for year, expected_day in known_equinoxes:
            with self.subTest(year=year):
                day = astronomy.calculate_vernal_equinox(year)
                self.assertEqual(day, expected_day,
                               f"Vernal equinox for {year} should be March {expected_day}, got {day}")

    def test_autumn_equinox_historical_dates(self):
        """Test autumn equinox dates against historical records."""
        # Known autumn equinox dates from Japanese astronomical almanac
        known_equinoxes = [
            (1980, 23),
            (1990, 23),
            (2000, 23),
            (2010, 23),
            (2020, 22),
            (2024, 22),
            (2025, 23),
        ]

        for year, expected_day in known_equinoxes:
            with self.subTest(year=year):
                day = astronomy.calculate_autumn_equinox(year)
                self.assertEqual(day, expected_day,
                               f"Autumn equinox for {year} should be September {expected_day}, got {day}")

    def test_vernal_equinox_extended_range(self):
        """Test vernal equinox calculations for extended year range."""
        # Test years from 1948 to 3000
        test_years = [1948, 1950, 1980, 2000, 2050, 2100, 2200, 2500, 3000]

        for year in test_years:
            with self.subTest(year=year):
                day = astronomy.calculate_vernal_equinox(year)
                # Vernal equinox should be between March 19-21
                self.assertGreaterEqual(day, 19, f"Vernal equinox {day} too early for {year}")
                self.assertLessEqual(day, 21, f"Vernal equinox {day} too late for {year}")

    def test_autumn_equinox_extended_range(self):
        """Test autumn equinox calculations for extended year range."""
        # Test years from 1948 to 3000
        test_years = [1948, 1950, 1980, 2000, 2050, 2100, 2200, 2500, 3000]

        for year in test_years:
            with self.subTest(year=year):
                day = astronomy.calculate_autumn_equinox(year)
                # Autumn equinox should be between September 21-24
                self.assertGreaterEqual(day, 21, f"Autumn equinox {day} too early for {year}")
                self.assertLessEqual(day, 24, f"Autumn equinox {day} too late for {year}")

    def test_vernal_equinox_before_1948(self):
        """Test that vernal equinox returns 0 for years before 1948."""
        for year in [1900, 1920, 1947]:
            with self.subTest(year=year):
                day = astronomy.calculate_vernal_equinox(year)
                self.assertEqual(day, 0, f"Should return 0 for year {year}")

    def test_autumn_equinox_before_1948(self):
        """Test that autumn equinox returns 0 for years before 1948."""
        for year in [1900, 1920, 1947]:
            with self.subTest(year=year):
                day = astronomy.calculate_autumn_equinox(year)
                self.assertEqual(day, 0, f"Should return 0 for year {year}")

    def test_performance_vernal_equinox(self):
        """Test that vernal equinox calculation meets performance requirements."""
        # Requirement: < 1ms per calculation
        year = 2020
        iterations = 100

        start_time = time.perf_counter()
        for _ in range(iterations):
            astronomy.calculate_vernal_equinox(year)
        end_time = time.perf_counter()

        avg_time_ms = (end_time - start_time) * 1000 / iterations
        self.assertLess(avg_time_ms, 1.0,
                       f"Average calculation time {avg_time_ms:.3f}ms exceeds 1ms requirement")

    def test_performance_autumn_equinox(self):
        """Test that autumn equinox calculation meets performance requirements."""
        # Requirement: < 1ms per calculation
        year = 2020
        iterations = 100

        start_time = time.perf_counter()
        for _ in range(iterations):
            astronomy.calculate_autumn_equinox(year)
        end_time = time.perf_counter()

        avg_time_ms = (end_time - start_time) * 1000 / iterations
        self.assertLess(avg_time_ms, 1.0,
                       f"Average calculation time {avg_time_ms:.3f}ms exceeds 1ms requirement")

    def test_consistency_across_years(self):
        """Test that equinox calculations are consistent across consecutive years."""
        # Check that the difference between consecutive years is reasonable
        for year in range(2000, 2030):
            with self.subTest(year=year):
                day1 = astronomy.calculate_vernal_equinox(year)
                day2 = astronomy.calculate_vernal_equinox(year + 1)

                # The difference should be at most 2 days (accounting for leap years)
                diff = abs(day2 - day1)
                self.assertLessEqual(diff, 2,
                                   f"Vernal equinox dates differ by {diff} days between {year} and {year+1}")

    def test_solar_anomaly(self):
        """Test solar mean anomaly calculation."""
        # At J2000.0, the mean anomaly should be close to 357.5°
        t = 0.0  # J2000.0
        m = astronomy.solar_anomaly(t)
        self.assertAlmostEqual(m, 357.52910, places=3)

    def test_earth_orbit_eccentricity(self):
        """Test Earth's orbital eccentricity calculation."""
        # At J2000.0, eccentricity should be approximately 0.0167
        t = 0.0  # J2000.0
        e = astronomy.earth_orbit_eccentricity(t)
        self.assertAlmostEqual(e, 0.0167, places=4)

    def test_vernal_equinox_complete_range_2000_2030(self):
        """Test vernal equinox for complete range 2000-2030."""
        # Known values from National Astronomical Observatory of Japan
        expected_dates = {
            2000: 20, 2001: 20, 2002: 21, 2003: 21, 2004: 20,
            2005: 20, 2006: 21, 2007: 21, 2008: 20, 2009: 20,
            2010: 21, 2011: 21, 2012: 20, 2013: 20, 2014: 21,
            2015: 21, 2016: 20, 2017: 20, 2018: 21, 2019: 21,
            2020: 20, 2021: 20, 2022: 21, 2023: 21, 2024: 20,
            2025: 20, 2026: 20, 2027: 21, 2028: 20, 2029: 20,
            2030: 20,
        }

        for year, expected_day in expected_dates.items():
            with self.subTest(year=year):
                day = astronomy.calculate_vernal_equinox(year)
                self.assertEqual(day, expected_day,
                               f"Vernal equinox for {year} should be March {expected_day}, got {day}")

    def test_autumn_equinox_complete_range_2000_2030(self):
        """Test autumn equinox for complete range 2000-2030."""
        # Known values from National Astronomical Observatory of Japan
        expected_dates = {
            2000: 23, 2001: 23, 2002: 23, 2003: 23, 2004: 23,
            2005: 23, 2006: 23, 2007: 23, 2008: 23, 2009: 23,
            2010: 23, 2011: 23, 2012: 22, 2013: 23, 2014: 23,
            2015: 23, 2016: 22, 2017: 23, 2018: 23, 2019: 23,
            2020: 22, 2021: 23, 2022: 23, 2023: 23, 2024: 22,
            2025: 23, 2026: 23, 2027: 23, 2028: 22, 2029: 23,
            2030: 23,
        }

        for year, expected_day in expected_dates.items():
            with self.subTest(year=year):
                day = astronomy.calculate_autumn_equinox(year)
                self.assertEqual(day, expected_day,
                               f"Autumn equinox for {year} should be September {expected_day}, got {day}")


if __name__ == '__main__':
    unittest.main()
