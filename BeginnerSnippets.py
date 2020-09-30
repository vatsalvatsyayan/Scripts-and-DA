def foo(x):
    def retfun(y):
        return y * x
    return retfun


def bar(f1, f2):
    def newfun(y):
        return f1(y) / f2(y)
    return newfun


def a(z):
    return z * 10


b = foo(2)
c = bar(a, b)
print(a(5))
print(b(5))
print(c(5))