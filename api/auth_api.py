from api.base_api import BaseApi

class AuthApi(BaseApi):
    def login(self, username: str, password: str):
        return self.post("/auth/login", json={
            "username": username,
            "password": password
        })

    def get_current_user(self, token: str):
        return self.get("/auth/me", headers={
            "Authorization": f"Bearer {token}"
        })