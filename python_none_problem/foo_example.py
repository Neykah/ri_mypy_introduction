from .foo import Foo


class FooException(Exception):
    ...


def get_a_foo(foo_id):
    if foo_id > 100:
        return Foo(foo_id)
    return None


def do_something_with(a_foo):
    return a_foo.x


def main():
    foo = get_a_foo(123)

    if foo is None:
        raise FooException("couldn't get a foo, oh no!")
    do_something_with(foo)
    print("Success")
