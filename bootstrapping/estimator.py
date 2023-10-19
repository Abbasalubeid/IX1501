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
    if a + mu_estimator < mean_bootstrap < b + mu_estimator:
        count += 1

p_estimate = count / m

print(f"Estimated μ: {mu_estimator:.2f}")
print(f"Probability of estimated μ lying in the interval ({mu_estimator + a}, {mu_estimator + b}): {p_estimate:.4f} or {p_estimate*100:.2f}%")

# Plot
plt.hist(bootstrap_means, bins=50, edgecolor='black', alpha=0.7) 
plt.axvline(x=mu_estimator, color='r', linestyle='-', label=f'Original μ: {mu_estimator:.2f}')
plt.axvline(x=mu_estimator+a, color='g', linestyle='--', label=f'Interval: {mu_estimator+a} to {mu_estimator+b}')
plt.axvline(x=mu_estimator+b, color='g', linestyle='--')
plt.xlabel('Bootstrap sample mean')
plt.ylabel('Frequency')
plt.title(f'Distribution of {m} bootstrapped sample means')
plt.legend()
plt.tight_layout()

plt.savefig('bar_chart_bootstrap_means.png', dpi=300)