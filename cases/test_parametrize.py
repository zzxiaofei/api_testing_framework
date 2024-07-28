import pytest

"""
pytest.mark.parametrize装饰器可以实现测试用例参数化
1.这里是一个实现检查一定的输入和期望输出测试功能的典型例子
"""


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ])
def test_parametrize(test_input, expected):
    assert eval(test_input) == expected


"""
mark.xfail 标记为失败的用例，预期结果也是失败，实际也是失败，显示xfailed
"""
# @pytest.mark.parametrize("test_input,expected", [
#                         ("3+5", 8),
#                         ("2+4", 6),
#                         pytest.param("6 * 9", 42, marks=pytest.mark.xfail),
#                         ])


"""
参数组合:
1.若要获得多个参数化的参数所有的组合，可以堆叠参数化装饰器
"""


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("测试数据组合：x->%s, y->%s" % (x, y))


if __name__ == "__main__":
    pytest.main(['-s', 'test_parametrize.py'])
