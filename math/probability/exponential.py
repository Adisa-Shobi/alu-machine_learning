#!/usr/bin/env python3
'''
Defines a class Exponential that represents an exponential distribution
'''


class Exponential:
    '''
    Represents an exponential distribution
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
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        '''
        Calculates the value of the PDF for a given time period
        '''
        if x < 0:
            return 0
        return self.lambtha * self._exp(-self.lambtha * x)

    def cdf(self, x):
        '''
        Calculates the value of the CDF for a given time period
        '''
        if x < 0:
            return 0
        return 1 - self._exp(-self.lambtha * x)

    def _exp(self, x):
        '''
        Compute the value of e raised to the power x
        '''
        return (2.7182818285 ** x)
