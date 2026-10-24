import allure
from api.cart_api import CartApi

@allure.feature("购物车模块")
class TestCart:

    @allure.story("查询用户购物车")
    @allure.title("根据用户ID查询购物车")
    def test_get_cart_by_user(self):
        resp = CartApi().get_cart_by_user(1)
        assert resp.status_code == 200
        body = resp.json()
        assert "carts" in body

    @allure.story("购物车不存在")
    @allure.title("查询不存在的购物车应返回404")
    def test_get_nonexistent_cart(self):
        resp = CartApi().get_cart_by_id(99999)
        assert resp.status_code == 404