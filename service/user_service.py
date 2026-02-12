from model.user import User

class UserService:

    @staticmethod
    def create_user(data):
        required = ["nome", "email", "cpf", "senha"]

        for field in required:
            if field not in data or not data[field]:
                return {"error": f"O campo '{field}' é obrigatório"}, 400

        user = {
            "nome": data["nome"],
            "email": data["email"],
            "cpf": data["cpf"],
            "senha": data["senha"]
        }

        User.add_user(user)

        return user, 201
    
    @staticmethod
    def list_users():
        return User.get_all_users(), 200
    
    @staticmethod
    def get_user_by_id(user_id):
        user = User.get_user_by_id(user_id)
        if not user:
            return {"error": "Usuário não foi encontrado, ID inválido"}, 404
        return user, 200
    
    @staticmethod
    def delete_user(user_id):
        deleted = User.delete_by_id(user_id)
        if not deleted:
            return {"error": "Usuário não encontrado, ID inválido"}, 404
        return {"message":"Usuário deletado com sucesso"}, 200