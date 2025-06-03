import conf_logging
import logging
import unittest
from datas import Data
from datetime import datetime
from datetime import timezone
from pathlib import Path
import datas

logger=logging.getLogger(__name__)

ROOT_DIR=Path(__file__).parents[1]
REFMAR_DIR=ROOT_DIR / "data" / "REFMAR"

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

    def test_reader(self):
        files=[f for f in REFMAR_DIR.glob("111_*.txt")]
        data_list=datas.reader(files)
        self.assertGreater(len(data_list),1000000)
        data1=Data(datetime(2022,1,1,hour=11,minute=10,second=0,tzinfo=timezone.utc),7.624) # 01/01/2022 11:10:00;7.624;3
        data2=Data(datetime(1991,6,22,hour=18,minute=42,second=0,tzinfo=timezone.utc),7.106) # 22/06/1991 18:42:00;7.106;3
        data3=Data(datetime(2024,11,26,hour=19,minute=20,second=0,tzinfo=timezone.utc),7.449) # 26/11/2024 19:20:00;7.449;3
        data4=Data(datetime(2006,9,20,hour=22,minute=0,second=0,tzinfo=timezone.utc),8.062) # 20/09/2006 22:00:00;8.062;3
        data5=Data(datetime(2008,3,15,hour=16,minute=10,second=0,tzinfo=timezone.utc),6.887) # 15/03/2008 16:10:00;6.887;3
        self.assertIn(data1,data_list)
        self.assertIn(data2,data_list)
        self.assertIn(data3,data_list)
        self.assertIn(data4,data_list)
        self.assertIn(data5,data_list)
        