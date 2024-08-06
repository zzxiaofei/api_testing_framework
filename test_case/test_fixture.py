import pytest
import requests

"""
定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()
fixture命名不要以test开头，跟用例区分开。fixture是有返回值，没有返回值默认为None。用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。
"""

"""
fixture当作参数传入
"""

# @pytest.fixture()
# def test1():
#     a = 'hello pytest'
#     return a
#
#
# def test2(test1):
#     assert test1 == 'hello pytest'


"""
如果用例需要用到多个fixture的返回数据，fixture也可以返回一个元祖，list或字典，然后从里面取出对应数据。

"""


@pytest.fixture()
def test3():
    a = 'hello pytest'
    b = '123456'
    print('传出a,b')
    return a, b


def test4(test3):
    u = test3[0]
    p = test3[1]
    assert u == 'hello pytest'
    assert p == '123456'


"""
分成多个fixture，然后在用例中传多个fixture参数
"""

# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# @pytest.fixture()
# def test2():
#     b = '123456'
#     print('传出b')
#     return b
#
#
# def test3(test1, test2):
#     u = test1
#     p = test2
#     assert u == 'leo'
#     assert p == '123456'
#     print('传入多个fixture参数正确')


"""
fixture互相调用
"""

# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# def test2(test1):
#     assert test1 == 'leo'
#     print('fixture传参成功')


# @pytest.fixture()
# def func():
#     print('ready to go')
#
#
# def test_request(func):
#     data_youdao = {
#         "text": "hello"
#     }
#     url = "https://dict.youdao.com/keyword/key"
#     r = requests.post(url, data_youdao)
#
#     assert r.status_code == 200
#     result = r.json()
#     assert result['code'] == 0
#     assert result['message'] == 'SUCCESS'
#     assert result['data'] == []


# def test_two():
#     assert 1 == 1
#     assert 1 != 2
#     assert 1 < 2
#     assert 2 > 1
#     # assert 1 >= 2
#     assert 1 <= 1
#     assert 'a' in 'abc'
#     assert 'a' not in 'bcd'
#     assert True is True
#     assert False is False

# def test_pytest():
#     expect = 1
#     actual = 2
#     assert expect == actual

"""
fixture的作用范围
    :scope: scope参数可以控制fixture的作用范围 session>module>class>function(default)
        :function: 每一个函数或方法都会调用
        :class: 每一个类调用一次，一个类中可以有多个方法
        :module: 每一个.py文件调用一次，该文件有多个function和class
        :session: 是多个文件调用一次，可以跨.py文件调用，每个py文件就是module

fixture源码详解
    :fixture（scope='function'，params=None，autouse=False，ids=None，name=None）
    :scope: 有四个级别参数"function"（默认），"class"，"module"，"session"
    :params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它
    :autouse: 如果True，则为所有测试激活fixture func可以看到它。如果为False则显示需要参考来激活fixture
    :ids:每个字符串id的列表，每个字符串对应于params这样他们就是测试ID的一部分。如果没有提供ID它们将从params自动生成
    :name: fixture的名称。这默认为装饰函数的名称。如果fixture在定义它的统一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽，
    解决这个问题的一种方法时将装饰函数命令"fixture_<fixturename>"然后使用"@pytest.fixture（name='<fixturename>'）"。
"""

"""
scope = "function"
@pytest.fixture() 如果不写参数，参数就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例之后运行
"""

#
# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# @pytest.fixture(scope='function')
# def test2():
#     b = '男'
#     print('\n传出b')
#     return b
#
#
# def test3(test1):
#     name = 'leo'
#     print('找到name')
#     assert test1 == name
#
#
# def test4(test2):
#     sex = '男'
#     print('找到sex')
#     assert test2 == sex

"""
fixture scope为class, 如果class里面有多个用例，都调用了次fixture，那么此fixture只在class里所有用例开始前执行一次
"""

# @pytest.fixture(scope='class')
# def test1():
#     b = '男'
#     print('传出了%s, 且只在class里所有用例开始前执行一次！！！' % b)
#     return b
#
#
# class TestCase:
#     def test3(self, test1):
#         name = '男'
#         print('找到name')
#         assert test1 == name
#
#     def test4(self, test1):
#         sex = '男'
#         print('找到sex')
#         assert test1 == sex


"""
fixture为module时，在当前.py脚本里面所有用例开始前只执行一次。
"""

# @pytest.fixture(scope='module')
# def test1():
#     b = '男'
#     print('传出了%s, 且在当前py文件下执行一次！！！' % b)
#     return b
#
#
# def test3(test1):
#     name = '男'
#     print('找到name')
#     assert test1 == name
#
#
# class TestCase:
#
#     def test4(self, test1):
#         sex = '男'
#         print('找到sex')
#         assert test1 == sex


"""
fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，
如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里。
conftest.py文件名称时固定的，pytest会自动识别该文件。放到项目的根目录下就可以全局调用了，如果放到某个package下，那就在改package内有效。
如果需要同时执行两个py文件，可以在cmd中在文件py文件所在目录下执行命令：pytest -s test_fixture.py test_fixture1.py
"""

"""
调用fixture的三种方法
1.
函数或类里面方法直接传fixture的函数参数名称
"""

# @pytest.fixture()
# def test1():
#     print('\n开始执行function')
#
#
# def test_a(test1):
#     print('---用例a执行---')
#
#
# class TestCase:
#
#     def test_b(self, test1):
#         print('---用例b执行')

"""
使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例: 在特定类上使用fixture
"""

# @pytest.fixture()
# def test1():
#     print('\n开始执行function')
#
#
# @pytest.mark.usefixtures('test1')
# def test_a():
#     print('---用例a执行---')
#
#
# @pytest.mark.usefixtures('test1')
# class TestCase:
#
#     def test_b(self):
#         print('---用例b执行---')
#
#     def test_c(self):
#         print('---用例c执行---')


"""
叠加 usefixtures
如果一个方法或者一个class用例想要同时调用多个fixture，可以使用@pytest.mark.usefixture()进行叠加。注意叠加顺序，先执行的放底层，后执行的放上层。

usefixtures与传fixture区别
如果fixture有返回值，那么usefixture就无法获取到返回值，这个是装饰器usefixture与用例直接传fixture参数的区别。
当fixture需要用到return出来的参数时，只能讲参数名称直接当参数传入，不需要用到return出来的参数时，两种方式都可以。
"""

# @pytest.fixture()
# def test1():
#     print('\n开始执行function1')
#
#
# @pytest.fixture()
# def test2():
#     print('\n开始执行function2')
#
#
# @pytest.mark.usefixtures('test1')
# @pytest.mark.usefixtures('test2')
# def test_a():
#     print('---用例a执行---')
#
#
# @pytest.mark.usefixtures('test2')
# @pytest.mark.usefixtures('test1')
# class TestCase:
#
#     def test_b(self):
#         print('---用例b执行---')
#
#     def test_c(self):
#         print('---用例c执行---')


"""
fixture自动使用autouse=True
当用例很多的时候，每次都传这个参数，会很麻烦。fixture里面有个参数autouse，默认是False没开启的，可以设置为True开启自动使用fixture功能，这样用例就不用每次都去传参了

autouse设置为True，自动调用fixture功能
"""

# @pytest.fixture(scope='module', autouse=True)
# def test1():
#     print('\n开始执行module')
#
#
# @pytest.fixture(scope='class', autouse=True)
# def test2():
#     print('\n开始执行class')
#
#
# @pytest.fixture(scope='function', autouse=True)
# def test3():
#     print('\n开始执行function')
#
#
# def test_a():
#     print('---用例a执行---')
#
#
# def test_d():
#     print('---用例d执行---')
#
#
# class TestCase:
#
#     def test_b(self):
#         print('---用例b执行---')
#
#     def test_c(self):
#         print('---用例c执行---')


"""
conftest.py的作用范围

一个工程下可以建多个conftest.py的文件，一般在工程根目录下设置的conftest文件起到全局作用。在不同子目录下也可以放conftest.py的文件，作用范围只能在改层级以及以下目录生效。

1.conftest在不同的层级间的作用域不一样
2.conftest是不能跨模块调用的（这里没有使用模块调用）

"""


class TestCase:
    def test_login(self):
        print('结束运行test_fixture.py')
