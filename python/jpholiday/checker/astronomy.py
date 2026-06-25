"""天文計算モジュールの互換シム。

春分・秋分の天文計算の実体は Rust 製（`jpholiday._rust.astronomy`）。既存の
`jpholiday.checker.astronomy` の公開 API を維持するため、Rust の関数をそのまま再公開する。

Reference: Jean Meeus, "Astronomical Algorithms", 2nd edition
Accuracy: ±1 day for years 1948-3000
"""
from jpholiday import _rust

_astronomy = _rust.astronomy

# ユリウス日・角度関連
julian_day = _astronomy.julian_day
julian_centuries_since_j2000 = _astronomy.julian_centuries_since_j2000
normalize_angle = _astronomy.normalize_angle
julian_day_to_datetime = _astronomy.julian_day_to_datetime

# 太陽位置関連
solar_mean_longitude = _astronomy.solar_mean_longitude
earth_orbit_eccentricity = _astronomy.earth_orbit_eccentricity
solar_anomaly = _astronomy.solar_anomaly
equation_of_center = _astronomy.equation_of_center
solar_ecliptic_longitude = _astronomy.solar_ecliptic_longitude
solar_ecliptic_longitude_rate = _astronomy.solar_ecliptic_longitude_rate

# 分点計算
calculate_vernal_equinox = _astronomy.calculate_vernal_equinox
calculate_autumn_equinox = _astronomy.calculate_autumn_equinox

__all__ = [
    "julian_day",
    "julian_centuries_since_j2000",
    "normalize_angle",
    "julian_day_to_datetime",
    "solar_mean_longitude",
    "earth_orbit_eccentricity",
    "solar_anomaly",
    "equation_of_center",
    "solar_ecliptic_longitude",
    "solar_ecliptic_longitude_rate",
    "calculate_vernal_equinox",
    "calculate_autumn_equinox",
]
