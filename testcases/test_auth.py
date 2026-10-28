import allure
from api.auth_api import AuthApi
from utils.request_util import load_config
from utils.extract_util import write_extract,read_extract


@allure.feature("认证模块")
class TestAuth:

    @allure.story("正常登录")
    @allure.title("使用正确账号密码登录")
    def test_login_success(self):
        config = load_config()
        env = config["active_env"]
        resp = AuthApi().login(
            config["env"][env]["username"],
            config["env"][env]["password"]
        )
        # 第一层：状态码
        assert resp.status_code == 200
        # 第二层：响应结构
        body = resp.json()
        assert "accessToken" in body
        # 第三层：业务字段
        assert len(body["accessToken"]) > 0

        #将token存入extract_util中，便于多接口调用
        write_extract(
            "token",body["accessToken"]
        )

    @allure.story("密码错误")
    @allure.title("使用错误密码登录应失败")
    def test_login_wrong_password(self):
        resp = AuthApi().login("emilys", "wrong_password_123")
        assert resp.status_code in [400, 401]

    @allure.story("Token鉴权")
    @allure.title("使用有效Token获取当前用户信息")
    def test_get_current_user(self, auth_token):
        resp = AuthApi().get_current_user(auth_token)
        assert resp.status_code == 200
        assert "username" in resp.json()