import sys

import pytest

"""
pytest.mark.skip可以标记无法在某些平台上运行的测试功能，或者您希望失败的测试功能
skip意味着只有在满足某些条件时才希望测试通过，否则pytest应该跳过运行测试。 常见示例是在非Windows平台上跳过仅限Windows的测试，或跳过测试依赖于当前不可用的外部资源（例如数据库）。
xfail意味着您希望测试由于某种原因而失败。 一个常见的例子是对功能的测试尚未实施，或尚未修复的错误。 当测试通过时尽管预计会失败（标有pytest.mark.xfail），它是一个xpass，将在测试摘要中报告。
pytest计数并分别列出skip和xfail测试。 未显示有关跳过/ xfailed测试的详细信息默认情况下，以避免混乱输出。 您可以使用-r选项查看与“short”字母对应的详细信息显示在测试进度中
pytest -rxXs # show extra info on xfailed, xpassed, and skipped tests
有关-r选项的更多详细信息，请运行pytest -h
"""


@pytest.mark.skip(reason='No way of currently testing this')  # 跳过单个测试
# def test_skip():
#     pass
@pytest.mark.skip(reason='Skip the whole class')
class TestSkip:
    def test_success(self):
        assert True


# 有条件的跳过某些内容
@pytest.mark.skipif(sys.version_info < (3, 8), reason='requires Python 3.8 or higher')
def test_function():
    assert True
    # if True:
    #     pytest.skip("unsupported configuration")


if __name__ == '__main__':
    pytest.main(['-s', "test_skip.py"])
