from Resturant import Review

class Resturant:
    def __init__(self, name):
        self.name = name

    def resturant_name(self):
        return self.name
    
    def reviews(self):
        return [review for review in Review.all if review.restaurant == self.name]
    
    def customers(self):
        return list(set([review.customer for review in Review.all if review.restaurant == self.name]))

the_hub = Resturant("The Hub")
the_hub.resturant_name()

print(the_hub.resturant_name())
print(the_hub.reviews())
print(the_hub.customers())
