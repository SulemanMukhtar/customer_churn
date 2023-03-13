import pandas as pd

# Load the data
df = pd.read_csv("data/customer_churn_data.csv")

# Drop irrelevant columns
df = df.drop(["customerID", "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
              "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
              "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod"], axis=1)

# Convert binary categorical columns to numeric
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# Convert categorical columns with more than two categories to numeric using one-hot encoding
df = pd.get_dummies(df, columns=["SeniorCitizen", "InternetServiceType"])

# Replace missing values with the median value
df = df.fillna(df.median())

# Save the cleaned data to a new CSV file
df.to_csv("data/customer_churn_data_cleaned.csv", index=False)
