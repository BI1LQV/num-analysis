from functools import reduce
from re import X

from numpy import zeros


class Interpolation:
    def __init__(self, xn, yn):
        self.xn = xn
        self.yn = yn
        cnTmp = zeros([len(xn), len(xn)])
        for i in range(len(xn)):
            cnTmp[i][0] = yn[i]
            for j in range(i):
                cnTmp[i][j+1] = (cnTmp[i][j]-cnTmp[i-1][j])/(xn[i]-xn[i-j-1])
        self.cn = list(map(lambda i: cnTmp[i][i], range(len(cnTmp))))  # 差商表对角线

    def lagrange(self, x):
        yt = 0
        for i in range(0, len(self.xn)):
            tmp = 1
            for j in range(0, len(self.xn)):
                if i == j:
                    continue
                tmp *= (x-self.xn[j])/(self.xn[i]-self.xn[j])
            yt += tmp*self.yn[i]
        return yt

    def newton(self, x):
        coffs = reduce(lambda pre, i: [
                       *pre, pre[-1]*(x-self.xn[i-1])
                       ], range(1, len(self.xn)), [1])
        units = map(lambda coff, c: coff*c, coffs, self.cn)
        return reduce(lambda sum, i: sum+i, units)


x = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
y = [0.22713, 3.5151, 8.3228, 14.1950, 20.6704, 27.2814, 33.5544, 39.0096]

interpolator = Interpolation(x, y)
print(interpolator.lagrange(3.2))
print(interpolator.newton(3.2))
