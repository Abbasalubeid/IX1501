import numpy as np
import matplotlib.pyplot as plt

data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
n = len(data)
m = 10000
a = -5
b = 5
mu_estimator = np.mean(data)

bootstrap_means = []  # To store means of each bootstrap sample
count = 0

# Bootstrapping
for _ in range(m):
    bootstrap_sample = np.random.choice(data, n, replace=True)
    mean_bootstrap = np.mean(bootstrap_sample)
    bootstrap_means.append(mean_bootstrap)
    if a < mean_bootstrap - mu_estimator < b:
        count += 1

p_estimate = count / m

print(f"Estimated μ: {mu_estimator:.2f}")
print(f"Probability of estimated μ lying in the interval ({mu_estimator + a}, {mu_estimator + b}): {p_estimate:.4f} or {p_estimate*100:.2f}%")


