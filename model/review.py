#!/usr/bin/python3

class Review:
    def __init__(self, review_id, place, user, rating, comment):
        self.review_id = review_id
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment

    def add_review(self, review):
        self.reviews.append(review)
        return self.reviews

    def update_review(self, review):
        self.reviews.append(review)
        return self.reviews
    
    def delete_review(self, review):
        self.reviews.remove(review)
        return self.reviews
    
    def modofy_review(self, review):
        self.reviews.append(review)
        return self.reviews
    
    def rating_review(self, review):
        self.reviews.append(review)
        return self.reviews
    
    def modify_rating(self, rating):
        self.reviews.append(rating)
        return self.reviews
    