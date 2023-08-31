class Review:

    all = []
    def __init__(self, resturant, customer, rating):
        self.resturant = resturant
        self.customer = customer
        self.rating = rating
        Review.all.append(self)

    def review_rating(self):
        return self.rating

    @classmethod
    def review_all(cls, review):
        return cls.all.append(review)
    
good = Review("The Hub", "Dennis", 9)

print(good.review_rating())
    


    