import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


class TestDatatype:
    @pytest.mark.smoke
    def test_defaults(self):
        """Using no parameters should invoke defaults """
        t1 = Task()
        t2 = Task(None, None, False, None)
        assert t1 == t2

    def test_member_access(self):
        """check .field functionality of namedtuple"""
        t = Task('buy milk', 'brain')
        assert t.summary == 'buy milk'
        assert t.owner == 'brain'
        assert (t.done, t.id) == (False, None)

    @pytest.mark.xfail()
    def test_asdict(self):
        """_asdict() should return a dictionary"""
        t_task = Task('do something', 'daniel', True, '31')
        t_dict = t_task._asdict()
        expected = {'summary': 'do something',
                    'owner': 'daniel',
                    'done': True,
                    'id': '31'}
        assert t_dict == expected

    @pytest.mark.skip
    def test_replace(self):
        """replace() should change passed in fields"""
        t_before = Task('finsh learning', 'do', True)
        t_after = t_before._replace(id=10, done=True)
        t_expected = Task('finsh learning', 'do', True, 10)
        assert t_after == t_expected


if __name__ == '__main__':
    pytest.main(['-v'])


"""
@pytest.mark.xfail()
@pytest.mark.skip()
@pytest.mark.run_these_please() 用于标记测试分组 pytest -v -m run_these_please



"""