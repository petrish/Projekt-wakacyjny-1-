from uzytkownik import MenagerUzytkownika

class Auth:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def login(self, username):
        user = self.user_manager.get_user(username)
        if user:
            print(f"Zalogowano jako {username} ({user['role']})")
            return user
        else:
            raise ValueError("Nieprawidłowa nazwa użytkownika.")
            
        
