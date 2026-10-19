import requests
import yaml
import logging
import os

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# 定位项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_config():
    config_path = os.path.join(BASE_DIR, "config", "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def send_request(method: str, url: str, **kwargs) -> requests.Response:
    """
    统一发送请求，自动加上 base_url 和超时
    method: "get" / "post" / "put" / "delete"
    url: 以 / 开头的路径，比如 "/products/1"
    """
    config = load_config()
    env = config["active_env"]
    base_url = config["env"][env]["base_url"]
    timeout = config["env"][env].get("timeout", 10)

    full_url = base_url + url
    logger.info(f"请求: {method.upper()} {full_url}")

    try:
        resp = requests.request(method, full_url, timeout=timeout, **kwargs)
        logger.info(f"响应状态码: {resp.status_code}")
        return resp
    except requests.exceptions.Timeout:
        logger.error(f"请求超时: {full_url}")
        raise
    except requests.exceptions.ConnectionError:
        logger.error(f"连接失败: {full_url}")
        raise