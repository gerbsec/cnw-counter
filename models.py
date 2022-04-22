from dataclasses import dataclass


@dataclass(frozen=False)
class User:
    name: str
    total: int = 0

