import numpy as np
from scipy.stats import ttest_1samp

# Data
weights = np.array([54, 56, 52, 55, 58, 53, 57, 54, 55, 56])

# Perform one-sample t-test
t_stat, p_value = ttest_1samp(weights, popmean=55)

print("T-value:", t_stat)
print("P-value:", p_value)

# Interpretation at 0.05 significance
alpha = 0.05
if p_value < alpha:
    print("Result: Reject H0 → Diet changed weight.")
else:
    print("Result: Fail to reject H0 → Diet did NOT change weight.")
# =========================Using formula======================================================

# import numpy as np
# import math

# # Data
# weights = np.array([54, 56, 52, 55, 58, 53, 57, 54, 55, 56])
# n = len(weights)

# # STEP 1 — Mean
# mean_value = np.mean(weights)

# # STEP 2 — Standard Deviation (sample)
# # 2.1 deviations
# deviations = weights - mean_value

# # 2.2 squared deviations
# squared_dev = deviations ** 2

# # 2.3 variance (sample)
# variance = np.sum(squared_dev) / (n - 1)

# # 2.4 standard deviation
# sd = math.sqrt(variance)

# # STEP 3 — Standard Error
# SE = sd / math.sqrt(n)

# # STEP 4 — t-value
# mu = 55  # expected mean
# t_value = (mean_value - mu) / SE

# # PRINT RESULTS
# print("Sample Mean =", mean_value)
# print("Variance =", variance)
# print("Standard Deviation =", sd)
# print("Standard Error =", SE)
# print("t-value =", t_value)

# ===============================Finding P value Using Formula========================================================
# import math
# from scipy.stats import t

# data = [54, 56, 52, 55, 58, 53, 57, 54, 55, 56]
# mu0 = 55  # expected mean

# # 1. Mean
# mean = sum(data) / len(data)

# # 2. Variance (sample variance)
# variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)

# # 3. Standard deviation
# sd = math.sqrt(variance)

# # 4. Standard error
# se = sd / math.sqrt(len(data))

# # 5. t-value
# t_value = (mean - mu0) / se

# # 6. Degrees of freedom
# df = len(data) - 1

# # 7. p-value (two-tailed)
# p_value = 2 * t.sf(abs(t_value), df)

# print("Mean:", mean)
# print("Variance:", variance)
# print("SD:", sd)
# print("SE:", se)
# print("t-value:", t_value)
# print("p-value:", p_value)


