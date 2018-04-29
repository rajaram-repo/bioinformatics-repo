"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
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

def decorator_1(my_def):
    def internal_decorator_1():
        a = time.time()
        a_1=time.process_time()
        def_result = my_def()
        b_1=time.time()
        b = time.process_time()
        print(b_1-a)
        print(b-a_1)
        # print("'{}' finished in {} seconds".format(my_def.__name__, a - b))
        print(sys.getsizeof(def_result))
        return def_result
    return internal_decorator_1

@decorator_1
def squares():
    return [x**2 for x in range(1000000)]
# squares()

@decorator_1
def for_loop():
    new_list = []
    for i in range(1000000):
        new_list.append(i)
# for_loop()

@decorator_1
def for_loop_log():
    new_list = []
    for i in range(1000000):
        if i != 0:
            new_list.append(math.log10(i))
    # print(new_list)
# for_loop_log()

@decorator_1
def list_comp():
    new_list = [i for i in range(1000000)]
    # print(new_list)
# list_comp()

@decorator_1
def list_comp_log():
    new_list = [math.log(i) for i in range(1000000) if i != 0]
    # print(new_list)
# list_comp_log()

@decorator_1
def numpy_list():
    array = numpy.arange(1,1000000)
    # print(array)
# numpy_list()

@decorator_1
def numpy_list_log():
    array = numpy.arange(1,1000000)
    temp = numpy.log10(array)
    # print(temp)
# numpy_list_log()

@decorator_1
def pandas_list():
    array = numpy.arange(1, 1000000)
    # array_1 = pandas.Series.between(1,0,1000000,inclusive=True)
    array_2 = pandas.DataFrame(array)
    # print(array_2)
# pandas_list()

def pandas_list_log():
    array = numpy.arange(1, 1000000)
    temp = numpy.log10(array)
    # array_1 = pandas.Series.between(1,0,1000000,inclusive=True)
    array_2 = pandas.DataFrame(temp)
    # print(array_2)
# pandas_list_log()


@decorator_1
def generator_list():
    new_list = (i for i in range(1000000))
    # print(next(new_list))
    # print(next(new_list))
# generator_list()

@decorator_1
def generator_list_log():
    new_list = (math.log10(i) for i in range(1000000) if i != 0)
    # print(next(new_list))
    # print(next(new_list))
generator_list_log()