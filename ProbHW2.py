#ProbHW2

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # type: ignore

# Calculating population mean and variance 
mu = (0+1)/2
variance_pop = ((1-0)**2)/12


# Set up random variables 

numbers_array = np.random.uniform(size=(100,100))
a = np.array([-2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2])

# Calculating sample mean, sample variation, and Z_n
sample_mean=np.mean(numbers_array, axis = 1)
sample_var = variance_pop/100
Z_n = (sample_mean-mu) / np.sqrt(sample_var)

# Using loop to create arrays for probability 
print("Z_n",Z_n)
P_emp = []


for i in a:
    P_emp.append(np.sum(Z_n <= i) / 100)

print("Sample mean is ",sample_mean)
print("Sample variance is ", sample_var)
print(P_emp)
print(a)

# Start plotting 

x = np.linspace(-3,3,100)
plt.plot(x,norm.cdf(x), label='Empirical CDF (Simulation)') 
plt.plot(a,P_emp, marker = "o", label = 'Theoretical normal Distribution')
plt.title('Emperical: n=100, Trials= 100')
plt.xlabel('Critical Value a')
plt.ylabel('$P(Z_n \\leq a)$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()



