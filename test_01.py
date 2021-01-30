# 设置pytest作为单元测试工具
# 测试文件命名规则：test_*.py，*_test.py
# 测试类命名：Class Test():
# 测试方法及函数命名：test_
import pytest

import Calculator


class TestCalc:
    # 测试方法1
    def test_add(self):
        assert Calculator.add(1, 2) == 3

    # 非测试方法
    def notes(self):
        assert Calculator.add(10, 20) == 30


# 函数
def test_add1():
    assert Calculator.add(100, 200) == 300


def test_add2():
    assert Calculator.add(1, 0) == 0
# 执行方法有三种
# 【1】pytest执行
# 【2】python执行
# 【3】终端执行


if __name__ == '__main__':
    pytest.main("test_01.py")
