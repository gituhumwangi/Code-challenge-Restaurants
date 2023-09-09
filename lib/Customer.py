from Customer import Review 

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
    
    def restaurants(self):
        return list(set([review.restaurant for review in self.reviews]))
    
    def add_review(self, restaurant, rating):
        review = Review(restaurant, self, rating)  
        self.reviews.append(review) 

    def num_reviews(self):
        return len(self.reviews)
    
    def average_star_rating(self):
        if not self.reviews:
            return 0  
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)


    @classmethod
    def return_all(cls ,customer):
        return cls.all.append(customer)
    
    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all if customer.first_name == given_name]

    
name = Customer("Dennis", "Gituhu")

print(name.given_name())
print (name.last_name())
print(name.full_name())
print(Customer.all)
print(name.restaurants())
print(name.add_review())
