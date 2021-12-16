import math


def a(x):
    return x**2

lambdaA = lambda a: a ** 2;
print(lambdaA(5));


def b(x, y):
    return math.sqrt(x**2 + y**2)

lambdaB = lambda b, y: math.sqrt(b ** 2 + y ** 2);
print(lambdaB(5, 10));


def c(*args):
    return sum(args)/len(args)

lambdaC = lambda *args: sum(args)/len(args);
print(lambdaC(10));


def d(s):
    return "".join(set(s))

lambdaD = lambda s: ''.join(set(s));
print(lambdaD('iniString'));

