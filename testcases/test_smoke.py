from utils.request_util import send_request

def test_api_is_alive():
    """最基础的连通性测试"""
    resp = send_request("get", "/products?limit=1")
    assert resp.status_code == 200