#!/usr/bin/env python3
"""
defines Neuron class that defines
a single neuron performing binary classification
"""


import numpy as np


class Neuron:
    """
    Defines a single neuron to mimic binary classification

    class constructor
    """

    def __init__(self, nx):
        """
        Initializes a neuron given the number of input features

        this is usually how we define the input features in a neuron
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Getter for the private instance attribute __W
        """
        return (self.__W)

    @property
    def b(self):
        """
        Getter for the private instance attribute __b
        """
        return (self.__b)

    @property
    def A(self):
        """
        Getter for the private instance attribute __A
        """
        return (self.__A)

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron

        This serves as the output of the neuron
        """
        z = np.matmul(self.W, X) + self.b
        self.__A = 1 / (1 + (np.exp(-z)))
        return (self.A)
