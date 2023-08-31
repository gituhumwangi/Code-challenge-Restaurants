class Customer:
    all = list()

    def __init__(self, first_name,family_name):
        self._first_name = first_name
        self._family_name = family_name
        Customer.all.append(self)

    def given_name(self):
        return self._first_name
    
    def last_name(self):
        return self._family_name 

    def full_name(self):
        return f"{self.given_name()}  {self.last_name()}"

    @classmethod
    def return_all(cls ,customer):
        return cls.all.append(customer)
    
name = Customer("Dennis", "Gituhu")

print(name.given_name())
print (name.last_name())
print(name.full_name())
print(Customer.all)
