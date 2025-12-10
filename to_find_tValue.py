
import numpy as np
from scipy.stats import ttest_1samp

# Sample data (new changed weights)
weights = np.array([56, 54, 57, 55, 58, 59, 53, 54, 56, 57])

# Expected mean
mu = 55

# One Sample t-test
t_stat, p_value = ttest_1samp(weights, mu)

print("Sample Mean:", np.mean(weights))
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpretation at 0.05 significance
alpha = 0.05
if p_value < alpha:
    print("Result: Reject H0 → Diet changed weight.")
else:
    print("Result: Fail to reject H0 → Diet did NOT change weight.")

# =========================Using formula without p value======================================================

import numpy as np
import math

# Data (NEW WEIGHTS)
weights = np.array([56, 54, 57, 55, 58, 59, 53, 54, 56, 57])
n = len(weights)

# STEP 1 — Mean
mean_value = np.mean(weights)

# STEP 2 — Standard Deviation (sample)
# 2.1 deviations
deviations = weights - mean_value

# 2.2 squared deviations
squared_dev = deviations ** 2

# 2.3 variance (sample)
variance = np.sum(squared_dev) / (n - 1)

# 2.4 standard deviation
sd = math.sqrt(variance)

# STEP 3 — Standard Error
SE = sd / math.sqrt(n)

# STEP 4 — t-value
mu = 55  # expected mean
t_value = (mean_value - mu) / SE

# PRINT RESULTS
print("Sample Mean =", mean_value)
print("Variance =", variance)
print("Standard Deviation =", sd)
print("Standard Error =", SE)
print("t-value =", t_value)


# ===============================Finding P value Using Formula========================================================
import math
from scipy.stats import t

# Dataset chosen to give t ≈ 1.48
data = [56, 54, 57, 55, 58, 59, 53, 54, 56, 57]
mu0 = 55  # expected mean

# 1. Mean
mean = sum(data) / len(data)

# 2. Variance (sample variance)
variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)

# 3. Standard deviation
sd = math.sqrt(variance)

# 4. Standard error
se = sd / math.sqrt(len(data))

# 5. t-value
t_value = (mean - mu0) / se

# 6. Degrees of freedom
df = len(data) - 1

# 7. p-value (two-tailed)
p_value = 2 * t.sf(abs(t_value), df)

# PRINT RESULTS
print("Sample Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", sd)
print("Standard Error:", se)
print("t-value:", t_value)
print("p-value:", p_value)

# CONCLUSION
alpha = 0.05
if p_value < alpha:
    print("\nConclusion: Reject H0 → The new diet changed the average weight.")
else:
    print("\nConclusion: Fail to Reject H0 → The new diet did NOT change the average weight.")




