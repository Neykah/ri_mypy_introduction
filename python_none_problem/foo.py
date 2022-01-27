from dataclasses import dataclass


@dataclass(frozen=True)
class Foo:
    x: int
