from jpholiday.checker.interface import HolidayCheckerInterface
from jpholiday.registry.interface import CheckerRegistryInterface


class HolidayCheckerRegistry(CheckerRegistryInterface):
    """独自チェッカーのみを保持するレジストリ。

    組込み祝日・振替休日・国民の休日は Rust エンジンが計算するため、ここでは利用者が
    登録した独自チェッカーのみを型単位で重複排除しつつ保持する。
    """

    def __init__(self) -> None:
        self._checker: list[HolidayCheckerInterface] = []

    def checkers(self) -> list[HolidayCheckerInterface]:
        return self._checker

    def register(self, checker: HolidayCheckerInterface) -> None:
        if any(isinstance(h, type(checker)) for h in self._checker):
            return
        self._checker.append(checker)

    def unregister(self, checker: HolidayCheckerInterface) -> None:
        self._checker = [h for h in self._checker if not isinstance(h, type(checker))]
