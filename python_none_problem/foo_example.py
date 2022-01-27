from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Foo:
    x: int


class FooException(Exception):
    ...


def get_a_foo(foo_id: int) -> Optional[Foo]:
    if foo_id > 100:
        return Foo(foo_id)
    return None


def do_something_with(a_foo: Foo) -> int:
    return a_foo.x


def main() -> None:
    foo = get_a_foo(123)
    if foo is not None:
        do_something_with(foo)
    print("Success")
