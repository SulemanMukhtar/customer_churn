class Customer:
    def __init__(self, customer_id, gender, senior, partner, dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, paperless_billing, payment_method, monthly_charges, total_charges, churn):
        self.customer_id = customer_id
        self.gender = gender
        self.senior = senior
        self.partner = partner
        self.dependents = dependents
        self.tenure = tenure
        self.phone_service = phone_service
        self.multiple_lines = multiple_lines
        self.internet_service = internet_service
        self.online_security = online_security
        self.online_backup = online_backup
        self.device_protection = device_protection
        self.tech_support = tech_support
        self.streaming_tv = streaming_tv
        self.streaming_movies = streaming_movies
        self.contract = contract
        self.paperless_billing = paperless_billing
        self.payment_method = payment_method
        self.monthly_charges = monthly_charges
        self.total_charges = total_charges
        self.churn = churn

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.gender}, {self.senior}, {self.partner}, {self.dependents}, {self.tenure}, {self.phone_service}, {self.multiple_lines}, {self.internet_service}, {self.online_security}, {self.online_backup}, {self.device_protection}, {self.tech_support}, {self.streaming_tv}, {self.streaming_movies}, {self.contract}, {self.paperless_billing}, {self.payment_method}, {self.monthly_charges}, {self.total_charges}, {self.churn})"
