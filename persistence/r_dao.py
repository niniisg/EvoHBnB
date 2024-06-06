#!/usr/bin/python3

class ReviewDAO:
    def __init__(self):
        self.reviews = []

    def save_review(self, review):
        self.reviews.append(review)

    def get_reviews_for_place(self, place_id):
        return [review for review in self.reviews if review.place.place_id == place_id]

    def get_reviews_by_user(self, user_id):
        return [review for review in self.reviews if review.user.user_id == user_id]
