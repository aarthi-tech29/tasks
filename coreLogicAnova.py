import numpy as np
from scipy import stats

instagram = np.array([120, 130, 128, 125, 135])
google    = np.array([140, 150, 148, 145, 152])
newspaper = np.array([110, 108, 115, 112, 109])

f_stat, p_value = stats.f_oneway(instagram, google, newspaper)

print("F-Statistic:", round(f_stat, 4))
print("p-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print(" Reject H0: At least one ad type gives different average sales.")
else:
    print(" Fail to Reject H0: No significant difference in average sales.")

print("\nGroup Means:")
print("Instagram mean:", instagram.mean())
print("Google mean   :", google.mean())
print("Newspaper mean:", newspaper.mean())

