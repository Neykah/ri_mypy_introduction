from typing import Optional
from foo_example import Foo


class Bar:
    """Formats a Foo.

    You MUST call `.initialize_system()` before formatting your foo!
    """

    # my_foo: Optional[Foo]

    def __init__(self) -> None:
        self.my_foo: Optional[Foo] = None

    def initialize_system(self, foo: Foo) -> None:
        self.my_foo = foo

    def format_foo(self) -> str:
        assert self.my_foo is not None, "My foo is not initialized!"
        return f"My foo's x is {self.my_foo.x}!"


def main() -> None:
    bar = Bar()
    bar.format_foo()
