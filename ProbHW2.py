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
print("Emperial Probability",P_emp)


# Start plotting 
x = np.linspace(-3,3,100)
plt.plot(x,norm.cdf(x), label='Theoretical Normal Distribution') 
plt.plot(a,P_emp, marker = "o", label = 'Empirical Cumulative Distribution')
plt.title('Emperical vs Theoretical')
plt.xlabel('Critical Value a')
plt.ylabel('P(Z_n <= a)')
plt.legend()
plt.show()

#Set up N, variance and mean
N = 1000
r_v_normal = np.random.normal(0,1, size = N)
r_v_cauchy = np.random.standard_cauchy(size=N)


n_values = np.arange(1, N + 1)
sample_mean_normal = np.cumsum(r_v_normal) / n_values
sample_mean_cauchy = np.cumsum(r_v_cauchy) / n_values


# Plot sample mean, and theoretical mean of normal distribution


plt.plot(n_values, sample_mean_normal, label='Sample Mean Normal')
plt.plot(n_values, sample_mean_cauchy, label='Sample Mean Cauchy')
plt.axhline(y=0, color='red', label='Mean = 0')
plt.title('Emperical Mean vs Mean in Normal vs Cauchy Distrbution')
plt.xlabel('Sample Size(N)')
plt.ylabel('Sample Mean')
plt.legend()
plt.show()





