import pytest
import os
import shutil
import time
from allure_pytest import plugin as allure_plugin

if __name__ == "__main__":
    # 当前目录生成一个report文件夹，以及allure-report下生成保存报告所需要的测试数据
    pytest.main(['-s', "--alluredir=./report/allure_result"])
    # 将report目录下生成的json数据转换成html测试报告文件
    os.system("allure generate ./report/allure_result -o ./report/html_result/ --clean")
    # 打开报告。本机地址+自定义端口。
    os.system("allure open -h 127.0.0.1 -p 8083 ./report/html_result")
