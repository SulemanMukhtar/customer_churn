import csv
import random
from customer import Customer


def generate_data(num_customers):
    genders = ["Male", "Female"]
    yes_no = ["Yes", "No"]
    internet_services = ["DSL", "Fiber optic", "No"]
    contracts = ["Month-to-month", "One year", "Two year"]
    payment_methods = ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]

    # Generate random customer data
    customers = []
    for i in range(num_customers):
        customer_id = i + 1
        gender = random.choice(genders)
        senior = random.choice(yes_no)
        partner = random.choice(yes_no)
        dependents = random.choice(yes_no)
        tenure = random.randint(1, 72)
        phone_service = random.choice(yes_no)
        multiple_lines = random.choice(["No phone service", "No", "Yes"])
        internet_service = random.choice(internet_services)
        online_security = random.choice(["No internet service", "No", "Yes"])
        online_backup = random.choice(["No internet service", "No", "Yes"])
        device_protection = random.choice(["No internet service", "No", "Yes"])
        tech_support = random.choice(["No internet service", "No", "Yes"])
        streaming_tv = random.choice(["No internet service", "No", "Yes"])
        streaming_movies = random.choice(["No internet service", "No", "Yes"])
        contract = random.choice(contracts)
        paperless_billing = random.choice(yes_no)
        payment_method = random.choice(payment_methods)
        monthly_charges = round(random.uniform(18.0, 118.0), 2)
        total_charges = round(monthly_charges * tenure, 2)
        churn = random.choice(yes_no)

        customer = Customer(customer_id, gender, senior, partner, dependents, tenure, phone_service, multiple_lines,
                            internet_service, online_security, online_backup, device_protection, tech_support,
                            streaming_tv, streaming_movies, contract, paperless_billing, payment_method,
                            monthly_charges, total_charges, churn)
        customers.append(customer)

    # Write customer data to CSV file
    with open('data/customer_churn_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["customerID", "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService",
                         "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                         "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
                         "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"])
        for customer in customers:
            writer.writerow(
                [customer.customer_id, customer.gender, customer.senior, customer.partner, customer.dependents,
                 customer.tenure, customer.phone_service, customer.multiple_lines, customer.internet_service,
                 customer.online_security, customer.online_backup, customer.device_protection, customer.tech_support,
                 customer.streaming_tv, customer.streaming_movies, customer.contract, customer.paperless_billing,
                 customer.payment_method, customer.monthly_charges, customer.total_charges, customer.churn])

    print(f"Successfully generated {num_customers} customer data entries.")
