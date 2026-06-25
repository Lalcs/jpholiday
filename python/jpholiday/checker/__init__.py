"""祝日チェッカーパッケージ。

`astronomy` / `checker` サブモジュールを明示的にロードし、`import jpholiday` 後に
`jpholiday.checker.astronomy` や `jpholiday.checker.checker` を属性として参照できるようにする
（白箱テストとの後方互換のため）。
"""
from jpholiday.checker import astronomy, checker  # noqa: F401
