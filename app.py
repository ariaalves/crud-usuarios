from flask import Flask
from controller.user_controller import UserController

app = Flask(__name__)

app.add_url_rule('/users', view_func= UserController.create_user, methods=["POST"])
app.add_url_rule('/users', view_func= UserController.get_users, methods=["GET"])
app.add_url_rule('/users/<int:user_id>', view_func= UserController.get_user, methods=["GET"])
app.add_url_rule('/users/<int:user_id>', view_func= UserController.delete_user, methods=["DELETE"])

if __name__ == '__main__':
    app.run(debug=True)
