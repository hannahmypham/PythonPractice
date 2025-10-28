#ProbHW2

"""Use numpy.random or any other of your favorite library to generate uniform random
variables between [0, 1]. Suppose X¯
n be the sample mean of n such random variables. Find mean µ and
variance of X¯
n. Let Zn =
X¯ √ n−µ
Var(X¯n)
. For n = 100, do 100 trials of this experiment, and plot the number
of times Zn ≤ a for a = −2, −1, −0.5, −0.25.0, 0.25, 0.5, 1, 2. Plot the cumulative distribution function
of N (0, 1) and compare.
"""

import numpy as np
numbers_array = np.random.uniform(50)
print(numbers_array)