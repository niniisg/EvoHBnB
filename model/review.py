#!/usr/bin/python3
from model.BaseModel import BaseModel

class Review(BaseModel):
    def __init__(self, review_id, place, user, rating, comment, text):
        super().__init__()
        self.review_id = review_id
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment
        self.review = text

    def add_review(self, review):
        if not isinstance(review, Review):
            raise ValueError("Review must be an instance of Review")
        self.reviews = review
        return self.reviews

    def update_review(self, review):
        if review is None:
            raise ValueError("Review must not be empty")
        self.reviews.append(review)
        return self.reviews
    
    def delete_review(self, user, review):
        if review is isinstance(self.id, user.__class__):
            self.reviews.remove(review)
            print("Review succesfully deleted. (:CDR:)")
        return ''
    
    def modofy_review(self, review):
        self.reviews.append(review)
        return self.review
    
    def modify_rating(self, rating):
        self.reviews.append(rating)
        return self.reviews
    
def rating_review(self, rating):
    if not isinstance(rating, int) or rating < 1 or rating > 5:
        raise ValueError("Rating must be an integer")
    self.rating = rating
    return self.rating