import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the cleaned data
df = pd.read_csv("data/customer_churn_data_cleaned.csv")

# calculate the churn rate
churn_rate = df["Churn"].mean()
print(f"Churn rate: {churn_rate:.2%}")

# plot the distribution of numeric variables
numeric_cols = ["tenure", "MonthlyCharges"]
for col in numeric_cols:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[col], kde=True)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()

# plot the churn rate by categorical variables
cat_cols = ["gender", "SeniorCitizen", "Partner", "Dependents", "InternetService", "Contract", "PaymentMethod"]
for col in cat_cols:
    plt.figure(figsize=(8, 6))
    sns.barplot(x=col, y="Churn", data=df)
    plt.title(f"Churn rate by {col}")
    plt.xlabel(col)
    plt.ylabel("Churn rate")
    plt.show()
