#class to represent a review

class Review:
   all_reviews = []
   
   def __init__(self, customer, restaurant, rating):
          # Initialize a review with a customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        customer.reviews.append(self)
        restaurant.reviews.append(self)

        # (methods for rating, customer, restaurant)
        
    def rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews
