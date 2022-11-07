from cmath import e
import sys
sys.setrecursionlimit(10000)


def acc(t):
    return t+e**(-t)


def euler(t0, t1, y0, h, n=0):
    tNow = t0+h*n
    if tNow >= t1:
        return y0
    return euler(t0, t1, y0+h*(-y0+tNow+1), h, n+1)


def access(h):
    return abs(euler(0, 1, 1, h)-acc(1))/acc(1)


print(access(0.1))
print(access(0.01))
print(access(0.001))
