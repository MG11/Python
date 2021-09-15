
def myPowhelper(self, x, n):
    if n == 1:
        return x
    return self.myPowhelper(self, x * x, (n - 1))

def myPow(self, x: float, n: int):
    if n == 0:
        return 1
    if n < 0:
        x = self.myPowhelper(self, x, n * (-1))
        return 1 / x
    return self.myPowhelper(self, x, n)