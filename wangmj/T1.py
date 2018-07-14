def str(s):
    print("global str()")


def foo():
    def str(s):
        print("closure str()")
    str("dummy")


def bar():
    str("dummy")


foo()
bar()