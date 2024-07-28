import pytest
import os
import shutil

if __name__ == '__main__':
    try:
        # 删除之前的文件夹
        shutil.rmtree("report")
        print('清除之前报告')
    except:
        pass
    pytest.main(['-s', 'test_allure.py'])
    # 直接生成报告html文件
    os.system('allure generate -o  report/re')
    # 编译报告原文件并启动报告服务
    os.system('allure serve report/allure_raw')
