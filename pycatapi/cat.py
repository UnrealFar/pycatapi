from dataclasses import dataclass

@dataclass(frozen=True)
class Cat:
    breeds: list
    id: str
    url: str
    width: int
    height: int
