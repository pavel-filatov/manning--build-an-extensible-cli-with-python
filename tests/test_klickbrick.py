import unittest

from klickbrick import __version__


class TestKlickbrick(unittest.TestCase):

    def test_version(self):
        assert __version__ == '0.1.0'
