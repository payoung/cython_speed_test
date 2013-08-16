cython_speed_test
=================

This repo contains some code I wrote to compare the performance of python code and cython code.

I modified the primes example in the cython tutorial[1] to run as both a pure python implementation, as well as a partial cython implementation.  I then pulled a timer python script from a website[2], and used the timer object to get the runtimes of the two implementations.  The run_test.py script loops through a range of input values (number of primes), and stores the performance of the two implementations.  I then plot the performance of the two implemntations against the in input value.  

The primary reason for putting this up here is for my own sake, as I imagine I will use this from time to time to get an idea of how cython can improve the performance of pthon code.

timer.py - conatins the timer object that I use to get the runtime of the python and cython function

py_primes.py - python function that takes an integer as input and returns the corresponding number of primes

cy_primes.pyx - cython function similar to py_primes.py (parts of the function are still written in python)

run_test.py - runs through a number of iterations of the py_primes.primes function and the cy_primes.primes function and returns the runtimes. the runtimes are plotted against the input values using matplotlib to get a vizualization of the comparative performance of the two implementations /n

[1] http://docs.cython.org/src/userguide/tutorial.html
[2] http://www.huyng.com/posts/python-performance-analysis/
