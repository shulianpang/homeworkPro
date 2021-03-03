import requests


def test_demo():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww50c8ee61b4922a5f&corpsecret=FyJmzf0NQ3B0n5_i0W0-_bPQX6x_aeCELMJ4GcUNMPo"
    r = requests.get(url)
    token = r.json()['access_token']

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {"userid": "zhangsan",
            "name": "张三",
            "department": [1],
            "mobile": "+86 13800000020"}
    r = requests.post(url, json=body)
    print(r.json())

    # 更新成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "李四"
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
    r = requests.get(url)
    print(r.json())

    # 查询成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=PangShuLian"
    r = requests.get(url)
