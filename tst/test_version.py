import unittest
import version

class TestVersion(unittest.TestCase):
    def test_version_major(self):
        self.assertEqual(version.MAJOR,0)

    def test_version_minor(self):
        self.assertEqual(version.MINOR,0)

    def test_version_build(self):
        self.assertEqual(version.BUILD,0)
