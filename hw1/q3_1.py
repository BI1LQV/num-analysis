EPISODE1 = 1e-16
EPISODE2 = 1e-16
START_AT = 1.8


def f(x): return x**2-3*x+2


def fixedPointIter(f, phy, x):
    xk = phy(x)
    if abs(f(x)) > EPISODE1 or abs(x-xk) > EPISODE2:
        return fixedPointIter(f, phy, xk)
    return xk


def phy1(x): return (x**2+2)/3
def phy2(x): return (3*x-2)**(1/2)
def phy3(x): return 3-2/x
def phy4(x): return (x**2-2)/(2*x-3)


phyList = [phy1, phy2, phy3, phy4]


def assess(fnList):
    def tryFn(fn, i):
        try:
            return fixedPointIter(f, fn, START_AT)
        except:
            return str(i+1)+" not pass"
    return list(map(tryFn, fnList, range(0, len(fnList))))


if __name__ == "__main__":
    print(assess(phyList))
