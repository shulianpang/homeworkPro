from test_requests.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    def test_add_member(self):
        # id, name, department, mobile,
        id = "zhangsan"
        name = "张三"
        department = [1]
        mobile = "+86 13800000020"
        r = self.address.add_member(id=id, name=name, department=department, mobile=mobile)
        assert r.get("errcode") == 0

    def test_read_member(self):
        id = "zhangsan"
        r = self.address.read_member(id)
        assert r.get('name') == "张三"

    def test_update_member(self):
        id = "zhangsan"
        name = "李四"
        department = [1]
        mobile = "+86 13800000020"
        r =  self.address.update_member(id, name, department, mobile)
        assert r.get("errcode") == 0

    def test_delete_member(self):
        userid = "zhangsan"
        r = self.address.delete_member(userid)
        assert r.get("errcode") == 0
