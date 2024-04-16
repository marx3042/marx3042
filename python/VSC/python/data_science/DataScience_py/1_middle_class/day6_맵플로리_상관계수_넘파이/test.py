import numpy as np

mu = 10
sigma = 2
randoms = mu + sigma * np.random.randn(5,4)
print(np.median(randoms))
print(np.mean(randoms))
print(randoms.mean())