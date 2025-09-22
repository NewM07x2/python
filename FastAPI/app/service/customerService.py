from app.models.customerModel import CustomerModel

class CustomerService:

    def __init__(self):
        self.customer = CustomerModel()

    def getCustomerData(self):
        
        return {
            # "id": self.id,
            # "name": self.name,
            # "email": self.email
        }
