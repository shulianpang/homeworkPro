from test_requests.api.base import Base


class Address(Base):

    def add_member(self, id, name, department, mobile, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {"userid": id,
                "name": name,
                "department": department,
                "mobile": mobile}
        return self.send('post', url, json=body)

    def delete_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send('get', url)

    def update_member(self, id, name, department, mobile, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {"userid": id,
                "name": name,
                "department": department,
                "mobile": mobile}
        return self.send('post', url, json=body)

    def read_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send('get',url)
