# Class to represent a restaurant

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        # Initialize a restaurant instance with a name
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

          # (methods for name, add_review, reviews, customers, average_star_rating)
    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list({review.customer for review in self.reviews})

    def get_average_star_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

# Define a class named Review to represent customer reviews for a restaurant.
class Review:
    def __init__(self, customer, rating):
        self.customer = customer
        self.rating = rating

#Example usage
# Create instances of Restaurant
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Add reviews for restaurants
review1 = Review("Customer 1", 4)
review2 = Review("Customer 2", 5)

restaurant1.add_review(review1)
restaurant2.add_review(review2)

# Print restaurant details
print("Restaurant 1:", restaurant1.name)
print("Restaurant 1 Reviews:", restaurant1.get_reviews())
print("Restaurant 1 Customers:", restaurant1.get_customers())
print("Restaurant 1 Average Rating:", restaurant1.get_average_star_rating())

print("Restaurant 2:", restaurant2.name)
print("Restaurant 2 Reviews:", restaurant2.get_reviews())
print("Restaurant 2 Customers:", restaurant2.get_customers())
print("Restaurant 2 Average Rating:", restaurant2.get_average_star_rating())
