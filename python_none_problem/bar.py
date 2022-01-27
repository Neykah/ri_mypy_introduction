from typing import Optional
from foo import Foo


class Bar:
    """Formats a Foo.

    You MUST call `.initialize_system()` before formatting your foo!
    """

    my_foo: Optional[Foo]

    def __init__(self):
        self.my_foo = None

    def initialize_system(self, foo: Foo) -> None:
        self.my_foo = foo

    def format_foo(self) -> str:
        return f"My foo's x is {self.my_foo.x}!"
