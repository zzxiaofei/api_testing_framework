import pytest
import allure

"""
1. 能够支持简单的单元测试和复杂的功能测试
2. 支持参数化
3. 执行测试过程中可以将某些测试跳过（skip），或者对某些预期失败的case标记成失败
4. 支持重复执行(rerun)失败的case
5. 支持运行由nose, unittest编写的测试case
6. 可生成html报告
7. 方便的和持续集成工具jenkins集成
8. 可支持执行部分用例
9. 具有很多第三方插件，并且可以自定义扩展
"""

class TestCase:

    @pytest.fixture(autouse=True)
    def setup(self):
        print('------>每个用例的前置')

    @pytest.fixture(autouse=True)
    def teardown(self):
        print('------>每个用例的后置')

    def test_a(self):  # test开头的测试函数
        print("------->test_a")
        assert 1  # 断言成功

    def test_b(self):
        print("------->test_b")
        assert 1 == 1  # 断言失败

    # 判断是否为真（1>2,不对，为假，所有用例错误）
    def test_c(self):
        assert 1 > 2

    # 判断不为真
    def test_d(self):
        assert not 1 > 2

    # 判断in后面的包含前面的
    def test_e(self):
        assert "1" in ["1", "2", "5"]

    # 等于
    def test_f(self):
        assert 1 == 1

    # 不等于
    def test_g(self):
        assert 1 == 1


if __name__ == '__main__':
    # pytest.main(['-s', 'test_case.py'])
    pytest.main(['-s', '--alluredir=./report/allure-results'])

"""
    主函数传参数格式pytest.main(["参数1","参数2"])
    -s  打印调试信息如：print
    -v  打印详细信息 test_case.py::Testdemo::test_1 PASSED 类名，方法名
    -n 多线程运行用例，我的好像有问题   , "-n=2"
    --reruns  重跑用例可以设置次数    ,'--reruns=2'
    -x 一个用例报错，后续用例执行停止 
    --maxfail 设置几个用例失败后停止  ,'--maxfail=2'
    -k 运行包含指定字符的用例         ,'-k=xx'
    --lf, --last-failed 只重新运行上次运行失败的用例（或如果没有失败的话会全部跑）
    --ff, --failed-first 运行所有测试，但首先运行上次运行失败的测试（这可能会重新测试，从而导致重复的fixture setup/teardown）
    
    Terminal 运行规则
    1. pytest 文件名/
    2. 执行某一个py文件下的用例
    3. -k 按关键词匹配 pytest -k "answer"
    4. 按节点运行： pytest test_mod.py::TestClass::test_method
    5. 标记表达式， pytest -m slow 将运行用@ pytest.mark.slow装饰器修饰的所有测试
    
    
    常用插件：
    pytest_html: 生成xml/html格式测试报告:pytest --html=用户路径/report.html 
    pytest-xdist：pytest-xdist多线程运行:    pytest test_skip.py -n 2   （安装pytest-xdist）
    pytest-ordering: 改变用例执行顺序
    pytest-rerunfailures: 失败重跑的
    pytest-repeat: 重复执行单个测试用例，并指定重复次数
    allure-pytest
"""
