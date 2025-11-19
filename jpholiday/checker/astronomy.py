"""
Astronomical calculations for equinoxes and solstices.

This module implements high-precision astronomical calculations using only
Python's standard library. It calculates the Sun's ecliptic longitude and
finds the exact moments of equinoxes using Newton's method.

Reference: Jean Meeus, "Astronomical Algorithms", 2nd edition
Accuracy: ±1 day for years 1948-3000
Dependencies: math, datetime (standard library only)
"""

import math
import datetime


# Constants
J2000 = 2451545.0  # Julian Day for epoch J2000.0 (2000-01-01 12:00:00 UTC)
DAYS_PER_JULIAN_CENTURY = 36525.0
DEGREES_TO_RADIANS = math.pi / 180.0


def julian_day(year: int, month: int, day: int, hour: float = 0.0) -> float:
    """
    Calculate Julian Day Number for a given date and time.

    Args:
        year: Year
        month: Month (1-12)
        day: Day of month
        hour: Hour of day (0-24, can be fractional)

    Returns:
        Julian Day Number

    Algorithm from Jean Meeus, "Astronomical Algorithms", Chapter 7
    """
    if month <= 2:
        year -= 1
        month += 12

    # Gregorian calendar correction
    a = year // 100
    b = 2 - a + (a // 4)

    jd = math.floor(365.25 * (year + 4716)) + \
         math.floor(30.6001 * (month + 1)) + \
         day + hour / 24.0 + b - 1524.5

    return jd


def julian_centuries_since_j2000(jd: float) -> float:
    """
    Calculate Julian centuries since J2000.0 epoch.

    Args:
        jd: Julian Day Number

    Returns:
        Julian centuries since J2000.0
    """
    return (jd - J2000) / DAYS_PER_JULIAN_CENTURY


def normalize_angle(angle: float) -> float:
    """
    Normalize angle to range [0, 360) degrees.

    Args:
        angle: Angle in degrees

    Returns:
        Normalized angle in degrees
    """
    angle = angle % 360.0
    if angle < 0:
        angle += 360.0
    return angle


def solar_mean_longitude(t: float) -> float:
    """
    Calculate the Sun's mean longitude.

    Args:
        t: Julian centuries since J2000.0

    Returns:
        Mean longitude in degrees

    VSOP87 theory coefficients
    """
    # L0 = mean longitude at epoch
    # Formula: L0 = 280.4665 + 36000.7698*T
    l0 = 280.4664567 + 36000.76982779 * t + \
         0.0003032028 * t * t + \
         t * t * t / 49931000.0

    return normalize_angle(l0)


def earth_orbit_eccentricity(t: float) -> float:
    """
    Calculate Earth's orbital eccentricity.

    Args:
        t: Julian centuries since J2000.0

    Returns:
        Eccentricity (dimensionless)
    """
    e = 0.016708634 - 0.000042037 * t - 0.0000001267 * t * t
    return e


def solar_anomaly(t: float) -> float:
    """
    Calculate the Sun's mean anomaly.

    Args:
        t: Julian centuries since J2000.0

    Returns:
        Mean anomaly in degrees
    """
    # M = mean anomaly of the Sun
    m = 357.52910 + 35999.05030 * t - \
        0.0001559 * t * t - \
        0.00000048 * t * t * t

    return normalize_angle(m)


def equation_of_center(t: float) -> float:
    """
    Calculate the equation of center (difference between true and mean anomaly).

    Args:
        t: Julian centuries since J2000.0

    Returns:
        Equation of center in degrees
    """
    m = solar_anomaly(t)
    m_rad = m * DEGREES_TO_RADIANS

    # Equation of center with multiple terms for higher accuracy
    c = (1.914600 - 0.004817 * t - 0.000014 * t * t) * math.sin(m_rad) + \
        (0.019993 - 0.000101 * t) * math.sin(2 * m_rad) + \
        0.000290 * math.sin(3 * m_rad)

    return c


def solar_ecliptic_longitude(jd: float) -> float:
    """
    Calculate the Sun's apparent ecliptic longitude.

    This is the primary function for determining the Sun's position along
    the ecliptic. The ecliptic longitude is:
    - 0° at the March equinox (Spring)
    - 90° at the June solstice (Summer)
    - 180° at the September equinox (Autumn)
    - 270° at the December solstice (Winter)

    Args:
        jd: Julian Day Number

    Returns:
        Apparent ecliptic longitude in degrees [0, 360)

    Algorithm combines:
    - Mean longitude
    - Equation of center (true anomaly correction)
    - Nutation and aberration corrections
    """
    t = julian_centuries_since_j2000(jd)

    # Mean longitude
    l0 = solar_mean_longitude(t)

    # Equation of center
    c = equation_of_center(t)

    # True longitude = Mean longitude + Equation of center
    true_longitude = l0 + c

    # Apparent longitude (includes nutation and aberration)
    # Nutation in longitude
    # Omega: Mean longitude of ascending node of Moon's orbit
    # Formula from Meeus: Ω = 125.04° - 1934.136°·T
    # where T is Julian centuries since J2000.0
    omega = 125.04 - 1934.136 * t
    omega_rad = omega * DEGREES_TO_RADIANS

    # Nutation correction (simplified formula from Meeus)
    # Coefficient -0.00478° represents amplitude of primary nutation term
    nutation = -0.00478 * math.sin(omega_rad)

    # Aberration correction
    aberration = -0.00569

    apparent_longitude = true_longitude + nutation + aberration

    return normalize_angle(apparent_longitude)


def solar_ecliptic_longitude_rate(jd: float, dt: float = 0.0001) -> float:
    """
    Calculate the rate of change of solar ecliptic longitude.

    This is used in Newton's method to find the exact time of equinoxes.

    Args:
        jd: Julian Day Number
        dt: Small time increment in days for numerical derivative

    Returns:
        Rate of change in degrees per day
    """
    lon1 = solar_ecliptic_longitude(jd - dt / 2)
    lon2 = solar_ecliptic_longitude(jd + dt / 2)

    # Handle wraparound at 0/360 degrees
    diff = lon2 - lon1
    if diff > 180:
        diff -= 360
    elif diff < -180:
        diff += 360

    return diff / dt


def find_equinox_solstice(year: int, target_longitude: float,
                          initial_month: int, initial_day: int) -> datetime.datetime:
    """
    Find the exact moment when the Sun reaches a specific ecliptic longitude.

    Uses Newton's method to iteratively refine the time when the Sun's
    ecliptic longitude equals the target value.

    Args:
        year: Year
        target_longitude: Target ecliptic longitude in degrees
                         (0=Spring, 90=Summer, 180=Autumn, 270=Winter)
        initial_month: Initial guess for month
        initial_day: Initial guess for day

    Returns:
        datetime.datetime object representing the moment of equinox/solstice
        in UTC timezone

    Algorithm: Newton's method
        jd_new = jd_old - f(jd) / f'(jd)
        where f(jd) = solar_longitude(jd) - target_longitude
    """
    # Initial guess
    jd = julian_day(year, initial_month, initial_day, 12.0)

    # Newton's method iteration
    max_iterations = 10
    tolerance = 0.00001  # ~0.86 seconds accuracy

    for _ in range(max_iterations):
        # Current longitude
        current_lon = solar_ecliptic_longitude(jd)

        # Calculate difference, handling wraparound
        diff = current_lon - target_longitude
        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360

        # Check convergence
        if abs(diff) < tolerance:
            break

        # Newton's method update
        rate = solar_ecliptic_longitude_rate(jd)
        jd = jd - diff / rate

    # Convert Julian Day back to datetime
    return julian_day_to_datetime(jd)


def julian_day_to_datetime(jd: float) -> datetime.datetime:
    """
    Convert Julian Day Number to datetime object.

    Args:
        jd: Julian Day Number

    Returns:
        datetime.datetime object in UTC

    Algorithm from Jean Meeus, "Astronomical Algorithms", Chapter 7
    """
    jd = jd + 0.5
    z = math.floor(jd)
    f = jd - z

    if z < 2299161:
        a = z
    else:
        alpha = math.floor((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - math.floor(alpha / 4)

    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)

    day = b - d - math.floor(30.6001 * e) + f

    if e < 14:
        month = int(e - 1)
    else:
        month = int(e - 13)

    if month > 2:
        year = int(c - 4716)
    else:
        year = int(c - 4715)

    # Extract day, hour, minute, second
    day_int = int(day)
    hour_frac = (day - day_int) * 24
    hour = int(hour_frac)
    minute_frac = (hour_frac - hour) * 60
    minute = int(minute_frac)
    second_frac = (minute_frac - minute) * 60
    second = int(second_frac)
    microsecond = int((second_frac - second) * 1000000)

    return datetime.datetime(year, month, day_int, hour, minute, second, microsecond)


def calculate_vernal_equinox(year: int) -> int:
    """
    Calculate the day of the vernal (spring) equinox in March.

    Args:
        year: Year (1948-3000 supported)

    Returns:
        Day of month (typically 19-21)
        0 if year is before 1948 (calculation not supported)
    """
    if year < 1948:
        return 0

    # Initial guess: March 20
    equinox_time = find_equinox_solstice(year, 0.0, 3, 20)

    # Convert to Japan Standard Time (UTC+9)
    # Japan observes the equinox date in JST
    jst_time = equinox_time + datetime.timedelta(hours=9)

    # Verify that the month is correct (should always be March for vernal equinox)
    if jst_time.month != 3:
        raise ValueError(
            f"Vernal equinox calculation resulted in unexpected month: "
            f"{jst_time.month} (expected 3). Year: {year}, Date: {jst_time}"
        )

    return jst_time.day


def calculate_autumn_equinox(year: int) -> int:
    """
    Calculate the day of the autumnal (fall) equinox in September.

    Args:
        year: Year (1948-3000 supported)

    Returns:
        Day of month (typically 22-24)
        0 if year is before 1948 (calculation not supported)
    """
    if year < 1948:
        return 0

    # Initial guess: September 23
    equinox_time = find_equinox_solstice(year, 180.0, 9, 23)

    # Convert to Japan Standard Time (UTC+9)
    # Japan observes the equinox date in JST
    jst_time = equinox_time + datetime.timedelta(hours=9)

    # Verify that the month is correct (should always be September for autumn equinox)
    if jst_time.month != 9:
        raise ValueError(
            f"Autumn equinox calculation resulted in unexpected month: "
            f"{jst_time.month} (expected 9). Year: {year}, Date: {jst_time}"
        )

    return jst_time.day
