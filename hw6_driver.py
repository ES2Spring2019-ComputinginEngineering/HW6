# HOMEWORK 6 --- ES2
# Driver
#
# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME:
# NUMBER OF HOURS TO COMPLETE:
# YOUR COLLABORATION STATEMENT(s):
#
#
#*****************************************

import numpy as np
from hw6_functions import moving_avg, merge_arrays, pendulum_period


# Test moving_avg
print('Testing Moving Average')
x = np.array([1,2,3,4,5,6,7,8])
test_1 = moving_avg(x, 3);
test_2 = moving_avg(x, 5);
ans_1 = np.array([1.5, 2, 3, 4, 5, 6, 7, 7.5])
ans_2 = np.array([2, 2.5, 3, 4, 5, 6, 6.5, 7])
print('Moving Average Test 1:\t', (test_1 == ans_1).all())
print('Moving Average Test 2:\t', (test_2 == ans_2).all())


#Test Merge arrays
print('Testing Merge Arrays')
odds = np.array([1,3,5,7,9])
evens = np.array([2,4,6,8,10])    
out = merge_arrays(odds, evens)
out_ans = x = np.array([1,2,3,4,5,6,7,8,9,10])
print('Merge Arrays Test 1:\t', (out == out_ans).all())

#Test Pendulum Period
print('Testing Pendulum Period')
length = np.array([1,2,3,4])
g = np.array([9.81, 4, 2, 12])
T = pendulum_period(length, g)
T_ans = np.array([2.006067, 4.442883, 7.695299, 3.627599])
print('Pendulum Period Test 1:\t', (np.around(T, 6) == T_ans).all())