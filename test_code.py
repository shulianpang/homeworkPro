from pycode.calculator import Calculator
import pytest
import yaml


def get_datas():
    with open('./test_code.yaml') as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add_datas"]
        sub_datas = datas["sub_datas"]
        mul_datas = datas['mul_datas']
        div_datas = datas['div_datas']
        ids = datas["myids"]
        print("\n取数据")
        return [add_datas, sub_datas, mul_datas, div_datas, ids]


class TestCode:

    def setup_class(self):
        print('\n开始计算')
        self.cal = Calculator()
        # get_datas()

    def teardown_class(self):
        print('\n计算结束')

    # @pytest.mark.parametrize("a,b,expect", get_datas()[0], ids=get_datas()[4])
    @pytest.mark.parametrize("a,b,expect", [(1, 2, 3), (-1, -2, -3), (1000, 100, 1100)])
    def test_add(self, a, b, expect):
        assert self.cal.add(a, b) == expect

    # @pytest.mark.parametrize("a,b,expect", [(1, 2, -1), (-1, -2, 1), (1000, 100, 900)])
    @pytest.mark.parametrize("a,b,expect", get_datas()[1], ids=get_datas()[4])
    def test_sub(self, a, b, expect):
        assert self.cal.sub(a, b) == expect

    # @pytest.mark.parametrize("a,b,expect", [(1, 2, 2), (-1, -2, 2), (1000, 100, 100000)])
    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_datas()[4])
    def test_mul(self, a, b, expect):
        assert self.cal.mul(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[3], ids=get_datas()[4])
    def test_div(self, a, b, expect):
        assert self.cal.div(a, b) == expect
