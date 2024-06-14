from flask import Flask
from models import user
from API.api import route_manager

app = Flask(__name__)
route_manager(app)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
    # Remember that port 8000 is for convinience as a dev. Reduces chances of conflict.
    # Example usage:

    # Create user instances (Eliminate this comment if this is the option)
    # user1 = User("Angel", "angel@examplemail.com", "password123")
    # print(user1)

    # user2 = User("Nissel", "nissel@examplemail.com", "passwordnissel")
    # print(user2)

    # Handle duplicate emails case.
    # try:
    #    user3 = User("Carlos", "nissel@examplemail.com", "passwordcarl")
    # except ValueError as e:
    #    print(e)

    pass #Placeholder for leaving the script running.
