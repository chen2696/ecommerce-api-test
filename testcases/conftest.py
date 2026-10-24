import pytest
from api.auth_api import AuthApi
from utils.request_util import load_config

# 得到了登录的token，
@pytest.fixture(scope="session")
def auth_token():
    """登录一次，整个测试会话复用"""
    config = load_config()
    env = config["active_env"]
    username = config["env"][env]["username"]
    password = config["env"][env]["password"]

    resp = AuthApi().login(username, password)
    assert resp.status_code == 200, f"登录失败: {resp.text}"
    return resp.json()["accessToken"]

@pytest.fixture(scope="session")
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}