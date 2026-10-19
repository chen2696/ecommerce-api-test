from api.base_api import BaseApi

class ProductApi(BaseApi):
    def get_all_products(self, limit=30, skip=0):
        return self.get(f"/products?limit={limit}&skip={skip}")

    def get_product_by_id(self, product_id: int):
        return self.get(f"/products/{product_id}")

    def search_products(self, keyword: str):
        return self.get(f"/products/search?q={keyword}")