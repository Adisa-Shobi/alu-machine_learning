#!/usr/bin/env python3
'''
Computes multinormal
'''
import numpy as np


class MultiNormal:
    '''
    Class that represents a Multivariate Normal distribution
    '''
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        self.d = d

        # Calculate covariance matrix without using numpy.cov
        centered_data = data - self.mean
        self.cov = np.dot(centered_data, centered_data.T) / (n - 1)

        # Precompute values for PDF calculation
        self.cov_det = np.linalg.det(self.cov)
        self.cov_inv = np.linalg.inv(self.cov)

    def pdf(self, x):
        '''
        Calculates the PDF at a data point
        '''
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        if x.shape != (self.d, 1):
            raise ValueError(f"x must have the shape ({self.d}, 1)")

        # Calculate the PDF
        diff = x - self.mean
        exponent = -0.5 * np.dot(np.dot(diff.T, self.cov_inv), diff)
        coefficient = 1 / ((2 * np.pi) ** (self.d / 2) * np.sqrt(self.cov_det))

        return float(coefficient * np.exp(exponent))