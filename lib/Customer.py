#class to represent a customer

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
          # Initialize a customer instance with given name and family name
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

           # (methods for given_name, family_name, full_name, all, restaurants, add_review, num_reviews, find_by_name, find_all_by_given_name)

    def get_given_name(self):
        return self._given_name

    def get_family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self.get_given_name()} {self.get_family_name()}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list({review.restaurant for review in self.reviews})

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating) 
        self.reviews.append(review)
        restaurant.add_review(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name().strip().lower() == name.strip().lower():
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.get_given_name().strip().lower() == name.strip().lower()]
