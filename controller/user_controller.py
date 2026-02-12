from flask import request, jsonify
from service.user_service import UserService

class UserController:

    @staticmethod
    def create_user():
        data = request.get_json()
        response, status = UserService.create_user(data)
        return jsonify(response), status
    
    @staticmethod
    def get_users():
        response, status = UserService.list_users()
        return jsonify(response), status
    
    @staticmethod
    def get_user(user_id):
        response, status = UserService.get_user_by_id(user_id)
        return jsonify(response), status
    
    @staticmethod
    def delete_user(user_id):
        response, status = UserService.delete_user(user_id)
        return jsonify(response), status
    
    
