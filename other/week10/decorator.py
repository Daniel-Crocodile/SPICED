"""
Simple example of a decorator.
"""

import time


def decorator_function(func):
    # The decorator function takes the function func as an input parameter
    def wrapper_function(*args, **kwargs):
        # The wrapper_function adds functionality to the original function
        result = func + added_functionality
        return result

    return wrapper_function


def function_timer(func):
    def wrapper_function(x):
        starting_time = time.time()
        func(x)
        end_time = time.time()
        print(f"The function took {starting_time - end_time} to run")

    return wrapper_function


@function_timer
def wait(x):
    time.sleep(x)


wait(1)


def same_as_wait(x):
    time.sleep(x)


waiter = function_timer(same_as_wait)
type(waiter)
waiter(1)
