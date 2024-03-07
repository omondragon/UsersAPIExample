from flask import Blueprint, request, jsonify
from users.models.user_model import Users
from users.models.db import db

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/api/users', methods=['GET'])
def get_users():
    print("listado de usuarios")
    users = Users.query.all()
    result = [{'name': user.name, 'email': user.email, 'username': user.username} for user in users]
    return jsonify(result)

@user_controller.route('/api/users', methods=['POST'])
def create_user():
    print("creando usuario")
    data = request.json
    #new_user = Users(name="oscar", email="oscar@gmail", username="omondragon", password="123")
    new_user = Users(name=data['name'], email=data['email'], username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

