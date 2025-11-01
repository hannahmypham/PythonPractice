import numpy as np
import matplotlib.pyplot as plt


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

