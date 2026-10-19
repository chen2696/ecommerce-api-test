from api.base_api import BaseApi

class CartApi(BaseApi):
    def get_cart_by_user(self, user_id: int):
        return self.get(f"/carts/user/{user_id}")

    def get_cart_by_id(self, cart_id: int):
        return self.get(f"/carts/{cart_id}")