import pyximport; pyximport.install()
import cy_primes
import py_primes
from timer import Timer
import matplotlib.pyplot as plt
import numpy as np

itrs = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

py_times = []
cy_times = []

for itr in itrs:

    with Timer() as t:
        cy_result = cy_primes.primes(itr)
    print "=> elapsed cython primes: %s s" % t.secs
    cy_times.append(t.secs)

    with Timer() as t:
        py_result = py_primes.primes(itr)
    print "=> elapsed python primes: %s s" % t.secs
    py_times.append(t.secs)

    assert cy_result == py_result


plt.plot(itrs, py_times, 'g', label='Python Implementation')
plt.plot(itrs, cy_times, 'b', label='Cython Implementation')
legen = plt.legend(loc='upper left', shadow=True)
plt.ylabel('seconds')
plt.xlabel('# of Primes')
plt.xlim(0, max(itrs)*1.1)
plt.ylim(0, max(py_times)*1.1)

plt.show()





