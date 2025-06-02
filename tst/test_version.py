import conf_logging
import logging
import unittest
import version

logger=logging.getLogger(__name__)

class TestVersion(unittest.TestCase):
    def test_version_major(self):
        self.assertEqual(version.MAJOR,0)

    def test_version_minor(self):
        self.assertEqual(version.MINOR,0)

    def test_version_build(self):
        self.assertEqual(version.BUILD,4)

    def test_print_version(self):
        print(version.get_version())
        self.assertEqual(version.get_version(),f"{version.MAJOR}.{version.MINOR}.{version.BUILD}")
