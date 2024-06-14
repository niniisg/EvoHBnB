from flask import Flask, jsonify, request, abort
from flask_restx import Api
from API import Place, Review, User
from API import api


app = Flask(__name__)
api = Api(app)


@api.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_review_for_place(place_id):
    place = Place.get(place_id)
    if not place:
        abort(404)
    review_data = request.json
    review = Review.create(place_id=place_id, **review_data)
    return jsonify(review.to_dict()), 201

@api.route('/users/<int:user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    user = User.get(user_id)
    if not user:
        abort(404)
    return jsonify([review.to_dict() for review in user.reviews])

@api.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews_for_place(place_id):
    place = Place.get(place_id)
    if not place:
        abort(404)
    return jsonify([review.to_dict() for review in place.reviews])

@api.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.get(review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@api.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.get(review_id)
    if not review:
        abort(404)
    review_data = request.json
    review.update(**review_data)
    return jsonify(review.to_dict())


@api.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.get(review_id)
    if not review:
        abort(404)
    review.delete()
    return jsonify({'message': 'Review deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True
