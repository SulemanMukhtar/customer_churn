import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# load the cleaned data
df = pd.read_csv("data/customer_churn_data_cleaned.csv")

# split the data into training and testing sets
X = df.drop("Churn", axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train a logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# make predictions on the testing set
y_pred = lr.predict(X_test)

# evaluate the model performance
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2%}")
print(classification_report(y_test, y_pred))
