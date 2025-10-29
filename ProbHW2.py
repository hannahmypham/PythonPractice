#ProbHW2

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

# Calculating population mean and variance 
variance_pop = ((1-0)**2)/12
mu = (0+1)/2

# Choose random variables 
np.random.seed(42)
numbers_array = np.random.uniform(size=(100,100))
a = np.array([-2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2])


sample_mean=np.mean(numbers_array, axis = 1)
sample_var = variance_pop/100
Z_n = (sample_mean- mu) / np.sqrt(sample_var)

P_emp = []
P_theo = []

print("Z_n",Z_n)

for i in a:
    P_emp.append(np.sum(Z_n <= i) / 100)
    P_theo.append(norm.cdf(i))

print("Sample mean is ",sample_mean)
print("Sample variance is ", sample_var)
print(P_emp)
print(P_theo)

