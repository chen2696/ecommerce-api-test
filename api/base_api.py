from utils.request_util import send_request

class BaseApi:
    def get(self, url, **kwargs):
        return send_request("get", url, **kwargs)

    def post(self, url, **kwargs):
        return send_request("post", url, **kwargs)

    def put(self, url, **kwargs):
        return send_request("put", url, **kwargs)

    def delete(self, url, **kwargs):
        return send_request("delete", url, **kwargs)