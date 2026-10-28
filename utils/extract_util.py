import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACT_PATH = os.path.join(BASE_DIR, "extract.yaml")


def write_extract(key, value):
    """把数据写进小本本，如果没有本本，就自动建一个"""
    data = {}
    # 核心逻辑：如果文件已经存在，就先读出来
    if os.path.exists(EXTRACT_PATH):
        with open(EXTRACT_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

    # 更新数据
    data[key] = value

    # 写回去（如果刚才文件不存在，这一步会自动创建文件）
    with open(EXTRACT_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


def read_extract(key):
    """从小本本里读数据，如果没有本本，直接返回空"""
    if not os.path.exists(EXTRACT_PATH):
        return None

    with open(EXTRACT_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get(key)