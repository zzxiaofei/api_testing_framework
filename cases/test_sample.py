import pytest


def func(x):
    return x + 1


# def test_answer():
#     assert func(3) == 5
#
#
# def test_success():
#     assert func(4) == 5


"""
为了写关于引发异常的断言，可以使用pytest.raises作为上下文管理器，如下
如果我们要断言它抛的异常是不是预期的，比如执行：1/0,预期结果是抛异常：ZeroDivisionError: division by zero，那我们要断言这个异常，通常是断言异常的type和value值了。
这里1/0的异常类型是ZeroDivisionError，异常的value值是division by zero，于是用例可以这样设计
excinfo 是一个异常信息实例，它是围绕实际引发的异常的包装器。主要属性是.type、 .value 和 .traceback
注意：断言type的时候，异常类型是不需要加引号的，断言value值的时候需转str
在上下文管理器窗体中，可以使用关键字参数消息指定自定义失败消息：
"""


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0
    print(excinfo)
    assert excinfo.type == ZeroDivisionError
    assert "division by zero" in str(excinfo.value)

    # with pytest.raises(ZeroDivisionError, message = "Expecting ZeroDivisionError") as excinfo:
    #     pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_sample.py'])
