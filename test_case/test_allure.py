# import pytest
# import allure
#
#
# @allure.step("步骤1:点xxx")
# def step_1():
#     print("111")
#
#
# @allure.step("步骤2:点xxx")
# def step_2():
#     print("222")
#
#
# @allure.feature("编辑页面")
# class TestEditPage:
#     """编辑页面"""
#
#     @allure.story("这是一个xxx的用例")
#     def test_1(self, login):
#         """用例描述：先登录，再去执行xxx"""
#         step_1()
#         step_2()
#         print("xxx")
#
#     @allure.story("打开a页面")
#     def test_2(self, login):
#         """用例描述：先登录，再去执行yyy"""
#         print("yyy")
#
#
# if __name__ == "__main__":
#     pytest.main(['-s', 'test_allure.py', '--allure-dir=./test'])


# file_name: test_allure.py


import pytest
import allure


@pytest.fixture(scope="function")
def login():
    print("执行登录逻辑")
    yield
    print("执行退出登录逻辑")


@allure.feature("加入购物车")
def test_01(login):
    """
    先登录，再进行其他操作
    :param login:
    :return:
    """
    print("测试用例01正在执行")


@allure.feature("加入购物车")
def test_02():
    """
    不需要登录，直接操作
    :return:
    """
    print("测试用例02正在执行")


if __name__ == '__main__':
    pytest.main(['-s', 'test_allure.py'])
