import requests
import json
"""请求方法"""
class SendMethod:
    @staticmethod
    def send_method(method,url,data=None):
        # 格式化请求数据
        req_data = {
            "json":{json.dumps(data)}
        }
        if method == "post":
            response = requests.request(method=method, url=url,data=req_data)
        elif method == "get":
            response = requests.request(method=method, url=url)
        else:
            response = None

        return response.json()

if __name__ == '__main__':
    url="http://192.168.2.150:8080/game/api/mobileLogin"
    data={"A":"1"}
    SendMethod.send_method("post",url=url,data=data)