# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:32:31 2022

@author: lenovo
"""

import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    
    
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    m = len(values)
    cost_history = []
    
    for i in range(num_iterations):
        predicted_values = numpy.dot(features,theta)
        theta= theta- alpha/m * numpy.dot((predicted_values- values), features)
        cost= compute_cost(features, values, theta)
        cost_history.append(cost)
    return theta, pandas.Series(cost_history) # leave this line for the grader

data = pandas.read_csv("baseball_stats.csv")
features = data[["height", "weight"]]
values = data[["HR"]]
m = len(values)
theta= {"height": 1, "weight" : 1}
alpha = 0.1
print(gradient_descent(features,values, theta, alpha, 10))
