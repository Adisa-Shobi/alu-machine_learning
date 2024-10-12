#!/usr/bin/env python3
'''
Poisson Distribution
'''


class Poisson:
    '''
    Class Poisson
    '''
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
            
    def pmf(self, k):
        k = int(k)
        if k < 0:
            return 0
        return (self.exp(-self.lambtha) * (self.lambtha ** k)) / self.factorial(k)

    def exp(self, x):
        result = 1
        term = 1
        n = 1
        while abs(term) > 1e-10:
            term *= x / n
            result += term
            n += 1
        return result

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
