import numpy as np
from scipy import stats

# Stress scores before and after yoga
before = np.array([35, 38, 40, 36, 37])
after  = np.array([28, 30, 32, 29, 30])

# Significance level
alpha = 0.05

# Paired t-test
t_statistic, p_value = stats.ttest_rel(after, before)

print("Paired t-test Results")
print("---------------------")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Decision rule
if p_value < alpha:
    print("\nDecision: Reject the null hypothesis (H0)")
    print("Conclusion: Yoga practice significantly reduces stress levels.")
else:
    print("\nDecision: Fail to reject the null hypothesis (H0)")
    print("Conclusion: Yoga practice does not significantly reduce stress levels.")
