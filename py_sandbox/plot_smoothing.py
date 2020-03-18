'''
date: 200318
objective: create smoothed out version of plot using scipy's bsplines
'''

from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import matplotlib.pyplot as plt
T = np.array([6, 7, 8, 9, 10, 11, 12])
power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])

# key lines: create new x and y values based on originals
xnew = np.linspace(T.min(), T.max(),len(T)*10)
spl = make_interp_spline(T, power, k=3)  # type: BSpline
power_smooth = spl(xnew)

plt.plot(T,power,label='original')
plt.plot(xnew, power_smooth,label='smoothed')
plt.legend()
plt.show()
