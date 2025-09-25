from app.models.customerModel import CustomerModel

class CustomerService:

    def __init__(self):
        self.customer = CustomerModel()

    def getCustomerData(self):
        return {
            "id": self.customer.id,
            "name": self.customer.name,
            "email": self.customer.email
        }
