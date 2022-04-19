from dataclasses import dataclass


@dataclass(frozen=False)
class User:
    name: str
    wallah: int = 0
    fword: int = 0
    sword: int = 0
    aword: int = 0