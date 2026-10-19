import allure
from api.product_api import ProductApi

@allure.feature("商品模块")
class TestProduct:

    @allure.story("查询商品列表")
    @allure.title("获取商品列表应返回正确数量")
    def test_get_all_products(self):
        resp = ProductApi().get_all_products(limit=5)
        assert resp.status_code == 200
        body = resp.json()
        assert "products" in body
        assert len(body["products"]) == 5

    @allure.story("查询商品详情")
    @allure.title("根据ID查询商品详情")
    def test_get_product_detail(self):
        resp = ProductApi().get_product_by_id(1)
        assert resp.status_code == 200
        body = resp.json()
        assert body["id"] == 1
        assert body["price"] > 0
        assert "title" in body

    @allure.story("商品不存在")
    @allure.title("查询不存在的商品应返回404")
    def test_get_nonexistent_product(self):
        resp = ProductApi().get_product_by_id(99999)
        assert resp.status_code == 404

    @allure.story("搜索商品")
    @allure.title("根据关键词搜索商品")
    def test_search_products(self):
        resp = ProductApi().search_products("phone")
        assert resp.status_code == 200
        body = resp.json()
        assert "products" in body