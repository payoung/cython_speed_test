cython_speed_test
=================

This repo contains some code I wrote to compare the performance of python code and cython code.

I modified the primes example in the cython tutorial[1] to run as both a pure python implementation, as well as a partial cython implementation.  I then pulled a timer python script from a website[2], and used the timer object to get the runtimes of the two implemntations.  The run_test.py script loops through a range of input values (number of primes), and stores the performance of the two implementations.  I then plot the performance of the two implemntations against the in input value.  

The primary reason for putting this up here is for my own sake, as I imagine I will use this from time to time to get an idea of how cython can improve the performance of pthon code.

[1] http://docs.cython.org/src/userguide/tutorial.html
[2] http://www.huyng.com/posts/python-performance-analysis/
