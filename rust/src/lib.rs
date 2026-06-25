//! jpholiday の Python バインディング（PyO3）。
//!
//! 上流の純 Rust クレート [`jpholiday`](https://crates.io/crates/jpholiday) を薄くラップし、
//! Python から呼べる `_rust` 拡張モジュールとして公開する。祝日判定・天文計算のロジックは
//! 一切ここで再実装せず、すべて上流クレートに委譲する。
//!
//! 公開する関数:
//! - [`holidays_on`] — 指定日に該当する組込み祝日（振替休日・国民の休日を含む）の名称一覧。
//!   独自チェッカーは Python 側で管理するためここには含めない。
//! - サブモジュール `astronomy` — 春分・秋分の天文計算関数（白箱テスト互換のため公開）。

use jpholiday::astronomy;
use jpholiday::Date;
use pyo3::prelude::*;
use pyo3::types::{PyDateTime, PyModule};
use pyo3::wrap_pyfunction;

/// 指定日（年・月・日）に該当する組込み祝日の名称一覧を返す。
///
/// 上流のグローバル API [`jpholiday::holidays`] に委譲する。返るのは組込み祝日・振替休日・
/// 国民の休日のみで、独自チェッカー（Python 側で管理）は含まない。実在しない日付の場合は
/// 空リストを返す（呼び出し側の Python ラッパが事前に有効な日付のみ渡す）。
#[pyfunction]
fn holidays_on(year: i32, month: u32, day: u32) -> Vec<String> {
    match Date::new(year, month, day) {
        Ok(date) => jpholiday::holidays(date)
            .into_iter()
            .map(|holiday| holiday.name)
            .collect(),
        Err(_) => Vec::new(),
    }
}

/// 指定日時のユリウス日を計算する。
#[pyfunction]
#[pyo3(signature = (year, month, day, hour = 0.0))]
fn julian_day(year: i64, month: i64, day: i64, hour: f64) -> f64 {
    astronomy::julian_day(year, month, day, hour)
}

/// J2000.0 元期からのユリウス世紀を返す。
#[pyfunction]
fn julian_centuries_since_j2000(jd: f64) -> f64 {
    astronomy::julian_centuries_since_j2000(jd)
}

/// 角度を `[0, 360)` の範囲へ正規化する。
#[pyfunction]
fn normalize_angle(angle: f64) -> f64 {
    astronomy::normalize_angle(angle)
}

/// 太陽の平均黄経を返す。
#[pyfunction]
fn solar_mean_longitude(t: f64) -> f64 {
    astronomy::solar_mean_longitude(t)
}

/// 地球軌道の離心率を返す。
#[pyfunction]
fn earth_orbit_eccentricity(t: f64) -> f64 {
    astronomy::earth_orbit_eccentricity(t)
}

/// 太陽の平均近点角を返す。
#[pyfunction]
fn solar_anomaly(t: f64) -> f64 {
    astronomy::solar_anomaly(t)
}

/// 中心差（equation of center）を返す。
#[pyfunction]
fn equation_of_center(t: f64) -> f64 {
    astronomy::equation_of_center(t)
}

/// 太陽の黄経を返す。
#[pyfunction]
fn solar_ecliptic_longitude(jd: f64) -> f64 {
    astronomy::solar_ecliptic_longitude(jd)
}

/// 太陽黄経の変化率を返す。
#[pyfunction]
#[pyo3(signature = (jd, dt = 0.0001))]
fn solar_ecliptic_longitude_rate(jd: f64, dt: f64) -> f64 {
    astronomy::solar_ecliptic_longitude_rate(jd, dt)
}

/// ユリウス日を `datetime.datetime`（UTC・naive）へ変換する。
#[pyfunction]
fn julian_day_to_datetime(py: Python<'_>, jd: f64) -> PyResult<Py<PyDateTime>> {
    let t = astronomy::julian_day_to_datetime(jd);
    let datetime = PyDateTime::new(
        py,
        t.year,
        t.month as u8,
        t.day as u8,
        t.hour as u8,
        t.minute as u8,
        t.second as u8,
        t.microsecond as u32,
        None,
    )?;
    Ok(datetime.unbind())
}

/// 春分の日（3 月）の日を返す。1948 年より前は 0。
#[pyfunction]
fn calculate_vernal_equinox(year: i32) -> u32 {
    astronomy::calculate_vernal_equinox(year)
}

/// 秋分の日（9 月）の日を返す。1948 年より前は 0。
#[pyfunction]
fn calculate_autumn_equinox(year: i32) -> u32 {
    astronomy::calculate_autumn_equinox(year)
}

/// `astronomy` サブモジュールを構築し、親モジュールへ登録する。
fn register_astronomy(parent: &Bound<'_, PyModule>) -> PyResult<()> {
    let py = parent.py();
    let module = PyModule::new(py, "astronomy")?;
    module.add_function(wrap_pyfunction!(julian_day, &module)?)?;
    module.add_function(wrap_pyfunction!(julian_centuries_since_j2000, &module)?)?;
    module.add_function(wrap_pyfunction!(normalize_angle, &module)?)?;
    module.add_function(wrap_pyfunction!(solar_mean_longitude, &module)?)?;
    module.add_function(wrap_pyfunction!(earth_orbit_eccentricity, &module)?)?;
    module.add_function(wrap_pyfunction!(solar_anomaly, &module)?)?;
    module.add_function(wrap_pyfunction!(equation_of_center, &module)?)?;
    module.add_function(wrap_pyfunction!(solar_ecliptic_longitude, &module)?)?;
    module.add_function(wrap_pyfunction!(solar_ecliptic_longitude_rate, &module)?)?;
    module.add_function(wrap_pyfunction!(julian_day_to_datetime, &module)?)?;
    module.add_function(wrap_pyfunction!(calculate_vernal_equinox, &module)?)?;
    module.add_function(wrap_pyfunction!(calculate_autumn_equinox, &module)?)?;
    parent.add_submodule(&module)?;
    // `import jpholiday._rust.astronomy` も解決できるよう sys.modules にも登録する。
    py.import("sys")?
        .getattr("modules")?
        .set_item("jpholiday._rust.astronomy", &module)?;
    Ok(())
}

/// Python 拡張モジュール `jpholiday._rust` のエントリポイント。
#[pymodule]
fn _rust(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(holidays_on, module)?)?;
    register_astronomy(module)?;
    Ok(())
}
