"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to  run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math

def decorator(def_in_inner_def):
    def inner_def():
        t0 = time.time()
        p0=time.process_time()
        def_result = def_in_inner_def()
        p1=time.process_time()
        t1 = time.time()
        print("'{}' finished in {} seconds".format(def_in_inner_def.__name__, t1 - t0))
        print("'{}' process finished in {} seconds".format(def_in_inner_def.__name__, p1 - p0))
        print(sys.getsizeof(def_result))
        return def_result
    return inner_def

@decorator
def for_loop():
    x = []
    for i in range(1,1000001):
        x.append(i)
    return x

@decorator
def list_comp():
    return [i for i in range(1, 1000001)]

@decorator
def numpy_list():
    return numpy.arange(1, 1000001)

@decorator
def pandas_list():
    return pandas.DataFrame([i for i in range(1,1000001)])

@decorator
def generator_list():
    return (i for i in range(1, 1000001))

@decorator
def for_loop_log():
    return numpy.log10(for_loop())

@decorator
def list_comp_log():
    return numpy.log10(list_comp())

@decorator
def numpy_list_log():
    return numpy.log10(numpy_list())

@decorator
def pandas_list_log():
    return numpy.log10(pandas_list())

@decorator
def generator_list_log():
    x=generator_list()
    return (numpy.log10(i) for i in x)


for_loop()
list_comp()
numpy_list()
pandas_list()
generator_list()
for_loop_log()
list_comp_log()
numpy_list_log()
pandas_list_log()
generator_list_log()