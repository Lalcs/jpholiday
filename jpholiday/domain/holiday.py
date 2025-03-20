import dataclasses
import datetime


@dataclasses.dataclass(frozen=True)
class Holiday:
    date: datetime.date
    name: str

    def to_tuple(self) -> tuple[datetime.date, str]:
        return self.date, self.name
