from flask import flask
from flask import request
import uuid

app = Flask(__name__)

#one for get and one for post

@app.route('/review/<id>', methods = ['GET'])
def method(id):
    for review in reviews:
        if review["id"] == id:
            return review, 200
    return {"message": "User not found"}, 404

@app.route('/review', methods = ['POST'])
def method2():
    review = request.json
    if not review["overall_rating"] or review["overall_rating"] < 0 or review["overall_rating"] > 10:
        return {"message": "Error with overall rating"}, 404
    return {
        "id": uuid.uuid4(),, #randomly generated
        "user_id": review["id"],
        "review": review,
        "overall_rating": review["overall_rating"],
        "nutrition_rating": review["nutrition_rating"],
        "taste_rating": review["taste_rating"],
        "cafe_type": review["cafe_type"],
        "anonymous": review["anonymous"],
        "image": review["image"]
    }, 200

app.run(host='0.0.0.0', port=81, debug = True)