users_db = []

next_id = 1

class User:

    @staticmethod
    def add_user(user_data):
        global next_id

        user_data["id"] = next_id
        next_id += 1
        users_db.append(user_data)

    @staticmethod
    def get_all_users():
        return users_db
    
    @staticmethod
    def get_user_by_id(user_id):
        for user in users_db:
            if user["id"] == user_id:
                return user    
        return None
    
    @staticmethod
    def delete_by_id(user_id):
        for index, user in enumerate(users_db):
            if user["id"] == user_id:
                users_db.pop(index)
                return True
        return False