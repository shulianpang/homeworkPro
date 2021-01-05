import pytest
import yaml
import os

from calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + '/cal_data.yaml'
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    add_datas = datas["add_datas"]
    sub_datas = datas["sub_datas"]
    mul_datas = datas["mul_datas"]
    div_datas = datas["div_datas"]
    ids = datas["myids"]


@pytest.fixture(params=add_datas, ids=ids)
def get_add_datas(request):
    print('\n开始加法计算')
    data = request.param
    print(f"data:{data}")
    yield data
    print('\n加法计算结束')


@pytest.fixture(params=sub_datas, ids=ids)
def get_sub_datas(request):
    print('\n开始减法计算')
    data = request.param
    yield data
    print('\n减法计算结束')


@pytest.fixture(params=mul_datas, ids=ids)
def get_mul_datas(request):
    print('\n开始乘法计算')
    data = request.param
    yield data
    print('\n乘法计算结束')


@pytest.fixture(params=div_datas, ids=ids)
def get_div_datas(request):
    print('\n开始除法计算')
    data = request.param
    yield data
    print('\n除法计算结束')


@pytest.fixture(scope='module')
def get_calc():
    cal = Calculator()
    return cal
