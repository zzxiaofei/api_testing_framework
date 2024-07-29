import pytest
import os
import shutil
import time
from allure_pytest import plugin as allure_plugin

if __name__ == "__main__":

    pytest.main()
    os.system("allure generate ./temps -o ./report --clean")

    # # args = ["-v", "-s", "--alluredir=report/allure", "--clean-alluredir"]
    #
    # pytest.main(args=args, plugins=[allure_plugin])
    #
    # time.sleep(2)
    # # 生成 Allure 报告
    # allure_report_dir = "report"
    # os.system(f"allure generate {allure_report_dir} --clean")
    #
    # time.sleep(5)
    # os.system("allure open /Users/xiaofeizhang/PyProjects/api_testing_framework/allure-report/")  # 运行完直接打开报告
    #
    # """
    # # 未使用pyinstaller打包工具前的代码：
    # pytest.main()
    # os.system("allure generate report --clean")
    # """

