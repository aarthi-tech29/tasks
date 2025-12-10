import pandas as pd
from scipy.stats import chi2_contingency

# Observed data
data = {
    "Apple":   [40, 20],   # Teens, Adults
    "Samsung": [30, 60]    # Teens, Adults
}
# pd.crosstab(df["AgeGroup"], df["Brand"])

# Create DataFrame
df = pd.DataFrame(data, index=["Teens", "Adults"])
print("Observed Table:")
print(df)

# Chi-Square Test
chi2, p, dof, expected = chi2_contingency(df, correction=False)

print("\nChi-Square Value:", chi2)
print("p-value:", p)
print("Degrees of Freedom:", dof)
print("\nExpected Table:")
print(pd.DataFrame(expected, index=df.index, columns=df.columns))

# -------------------------------
# ANALYSIS & CONCLUSION
# -------------------------------
print("\n--- ANALYSIS ---")

# Statement about chi-square value
print(f"The chi-square value is {chi2:.2f}, which shows the difference between observed and expected values.")

# Statement about p-value
print(f"The p-value is {p:.6f}. Since the p-value is less than 0.05, the result is statistically significant.")

# Decision
if p < 0.05:
    print("We REJECT the Null Hypothesis (H0).")
    conclusion = "Age group and mobile brand preference are dependent."
else:
    print("We FAIL to Reject the Null Hypothesis (H0).")
    conclusion = "Age group and mobile brand preference are independent."

# Final conclusion
print("\n--- CONCLUSION ---")
print("Conclusion:", conclusion)

if p < 0.05:
    print("Teens prefer Apple more, and adults prefer Samsung more.")
