import conf_logging
import logging
import unittest
from datas import Data
from datetime import datetime
from datetime import timezone

logger=logging.getLogger(__name__)

class TestDatas(unittest.TestCase):
    def test_create_Data(self):
        t=datetime.now(timezone.utc)
        data=Data(t,6.8)
        self.assertEqual(data.t,t)
        self.assertEqual(data.height,6.8)

    def test_cope_with_naive(self):
        t=datetime.now()
        with self.assertRaises(ValueError) as cm:
            Data(t,0.0)
        e=cm.exception
        print(e)
