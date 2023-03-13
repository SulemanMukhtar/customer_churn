import subprocess

# Generate the seeded data
subprocess.call(["python", "data_generator.py"])

# Clean the data
subprocess.call(["python", "data_cleaning.py"])

# Analyze the data
subprocess.call(["python", "data_analysis.py"])

# Make predictions
subprocess.call(["python", "churn_prediction.py"])