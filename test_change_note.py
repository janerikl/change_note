import unittest
from change_note import ChangeNote


class TestChangeNote(unittest.TestCase):

    def setUp(self):
        """ setup any state specific to the execution of the given module."""
        self.cn = ChangeNote('whatup')

    def tearDown(self):
        """ teardown any state that was previously setup with a setup_module
        method.
        """
        self.cn = None

    def test_open(self):
        assert self.cn.open_file()


if __name__ == '__main__':
    unittest.main()
