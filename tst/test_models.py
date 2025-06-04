import conf_logging
import logging
import unittest
from models import Model
from models import Model_N3
from models import Model_N6
from models import Model_N10
from models import Model_N16
from models import Model_N24
from models import Model_N32
import models
import harmonics as H
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import random
from pathlib import Path

logger=logging.getLogger(__name__)

ROOT_DIR=Path(__file__).parents[1]
SER_DIR=ROOT_DIR / "data" / "ser"

class TestModels(unittest.TestCase):
    def test_create_Model(self):
        """
        Test nominal creation of Model.
        """
        Model([H.M0,H.M2,H.S2,H.N2])

    def test_create_Model_N3(self):
        m=Model_N3()
        self.assertIn(H.M0,m.harmonics) # 0
        self.assertIn(H.M2,m.harmonics) # 1
        self.assertIn(H.S2,m.harmonics) # 2
        self.assertIn(H.N2,m.harmonics) # 3
        self.assertEqual(len(m.harmonics),4)
        self.assertEqual(len(m.amplitudes_cos),4)
        self.assertEqual(len(m.amplitudes_sin),4)
        
    def test_create_Model_N6(self):
        m=Model_N6()
        self.assertIn(H.M0,m.harmonics) # 0
        self.assertIn(H.M2,m.harmonics) # 1
        self.assertIn(H.S2,m.harmonics) # 2
        self.assertIn(H.N2,m.harmonics) # 3
        self.assertIn(H.K1,m.harmonics) # 4
        self.assertIn(H.M4,m.harmonics) # 5
        self.assertIn(H.O1,m.harmonics) # 6
        self.assertEqual(len(m.harmonics),7)
        self.assertEqual(len(m.amplitudes_cos),7)
        self.assertEqual(len(m.amplitudes_sin),7)
        
    def test_create_Model_N10(self):
        m=Model_N10()
        self.assertIn(H.M0,m.harmonics) # 0
        self.assertIn(H.M2,m.harmonics) # 1
        self.assertIn(H.S2,m.harmonics) # 2
        self.assertIn(H.N2,m.harmonics) # 3
        self.assertIn(H.K1,m.harmonics) # 4
        self.assertIn(H.M4,m.harmonics) # 5
        self.assertIn(H.O1,m.harmonics) # 6
        self.assertIn(H.M6,m.harmonics) # 7
        self.assertIn(H.MK3,m.harmonics) # 8
        self.assertIn(H.S4,m.harmonics) # 9
        self.assertIn(H.MN4,m.harmonics) # 10
        self.assertEqual(len(m.harmonics),11)
        self.assertEqual(len(m.amplitudes_cos),11)
        self.assertEqual(len(m.amplitudes_sin),11)

    def test_create_Model_N16(self):
        m=Model_N16()
        self.assertIn(H.M0,m.harmonics) # 0
        self.assertIn(H.M2,m.harmonics) # 1
        self.assertIn(H.S2,m.harmonics) # 2
        self.assertIn(H.N2,m.harmonics) # 3
        self.assertIn(H.K1,m.harmonics) # 4
        self.assertIn(H.M4,m.harmonics) # 5
        self.assertIn(H.O1,m.harmonics) # 6
        self.assertIn(H.M6,m.harmonics) # 7
        self.assertIn(H.MK3,m.harmonics) # 8
        self.assertIn(H.S4,m.harmonics) # 9
        self.assertIn(H.MN4,m.harmonics) # 10
        self.assertIn(H.nu2,m.harmonics) # 11
        # self.assertIn(H.S6,m.harmonics) # 12
        self.assertIn(H.mu2,m.harmonics) # 13
        self.assertIn(H._2N2,m.harmonics) # 14
        self.assertIn(H.OO1,m.harmonics) # 15
        self.assertIn(H.lambda2,m.harmonics) # 16
        self.assertEqual(len(m.harmonics),16)
        self.assertEqual(len(m.amplitudes_cos),16)
        self.assertEqual(len(m.amplitudes_sin),16)

    def test_create_Model_N24(self):
        m=Model_N24()
        self.assertIn(H.M0,m.harmonics) # 0
        self.assertIn(H.M2,m.harmonics) # 1
        self.assertIn(H.S2,m.harmonics) # 2
        self.assertIn(H.N2,m.harmonics) # 3
        self.assertIn(H.K1,m.harmonics) # 4
        self.assertIn(H.M4,m.harmonics) # 5
        self.assertIn(H.O1,m.harmonics) # 6
        self.assertIn(H.M6,m.harmonics) # 7
        self.assertIn(H.MK3,m.harmonics) # 8
        self.assertIn(H.S4,m.harmonics) # 9
        self.assertIn(H.MN4,m.harmonics) # 10
        self.assertIn(H.nu2,m.harmonics) # 11
        # self.assertIn(H.S6,m.harmonics) # 12
        self.assertIn(H.mu2,m.harmonics) # 13
        self.assertIn(H._2N2,m.harmonics) # 14
        self.assertIn(H.OO1,m.harmonics) # 15
        self.assertIn(H.lambda2,m.harmonics) # 16
        self.assertIn(H.S1,m.harmonics) # 17
        self.assertIn(H.M1,m.harmonics) # 18
        self.assertIn(H.J1,m.harmonics) # 19
        self.assertIn(H.Mm,m.harmonics) # 20
        self.assertIn(H.Ssa,m.harmonics) # 21
        self.assertIn(H.Sa,m.harmonics) # 22
        self.assertIn(H.Msf,m.harmonics) # 23
        self.assertIn(H.Mf,m.harmonics) # 24
        self.assertEqual(len(m.harmonics),24)
        self.assertEqual(len(m.amplitudes_cos),24)
        self.assertEqual(len(m.amplitudes_sin),24)

    def test_create_Model_N32(self):
        m=Model_N32()
        self.assertIn(H.M0,m.harmonics) # 0
        self.assertIn(H.M2,m.harmonics) # 1
        self.assertIn(H.S2,m.harmonics) # 2
        self.assertIn(H.N2,m.harmonics) # 3
        self.assertIn(H.K1,m.harmonics) # 4
        self.assertIn(H.M4,m.harmonics) # 5
        self.assertIn(H.O1,m.harmonics) # 6
        self.assertIn(H.M6,m.harmonics) # 7
        self.assertIn(H.MK3,m.harmonics) # 8
        self.assertIn(H.S4,m.harmonics) # 9
        self.assertIn(H.MN4,m.harmonics) # 10
        self.assertIn(H.nu2,m.harmonics) # 11
        # self.assertIn(H.S6,m.harmonics) # 12
        self.assertIn(H.mu2,m.harmonics) # 13
        self.assertIn(H._2N2,m.harmonics) # 14
        self.assertIn(H.OO1,m.harmonics) # 15
        self.assertIn(H.lambda2,m.harmonics) # 16
        self.assertIn(H.S1,m.harmonics) # 17
        self.assertIn(H.M1,m.harmonics) # 18
        self.assertIn(H.J1,m.harmonics) # 19
        self.assertIn(H.Mm,m.harmonics) # 20
        self.assertIn(H.Ssa,m.harmonics) # 21
        self.assertIn(H.Sa,m.harmonics) # 22
        self.assertIn(H.Msf,m.harmonics) # 23
        self.assertIn(H.Mf,m.harmonics) # 24
        self.assertIn(H.rau1,m.harmonics) # 25
        self.assertIn(H.Q1,m.harmonics) # 26
        self.assertIn(H.T2,m.harmonics) # 27
        self.assertIn(H.R2,m.harmonics) # 28
        self.assertIn(H._2Q1,m.harmonics) # 29
        self.assertIn(H.P1,m.harmonics) # 30
        self.assertIn(H._2SM2,m.harmonics) # 31
        self.assertIn(H.M3,m.harmonics) # 32
        self.assertEqual(len(m.harmonics),32)
        self.assertEqual(len(m.amplitudes_cos),32)
        self.assertEqual(len(m.amplitudes_sin),32)

    def test_get_hour(self):
        self.assertAlmostEqual(0.0,models.get_hour(H.T0),delta=0.000001)
        self.assertAlmostEqual(0.0,models.get_hour(datetime(1900,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)),delta=0.000001)
        self.assertAlmostEqual(1.0,models.get_hour(datetime(1900,1,1,hour=1,minute=0,second=0,tzinfo=timezone.utc)),delta=0.000001)
        # self.assertAlmostEqual(100*365.2425*24,models.get_hour(datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)),delta=0.000001)

        now=datetime.now(timezone.utc)
        tnow=models.get_hour(now)
        t1=now+timedelta(hours=1)
        self.assertAlmostEqual(tnow+1.0,models.get_hour(t1),delta=0.000001)
        t2=now+timedelta(hours=24)
        self.assertAlmostEqual(tnow+24,models.get_hour(t2),delta=0.000001)
        t3=now+timedelta(minutes=30)
        self.assertAlmostEqual(tnow+0.5,models.get_hour(t3),delta=0.000001)
        t4=now+timedelta(days=70,hours=10,minutes=30)
        self.assertAlmostEqual(tnow+70*24+10.5,models.get_hour(t4),delta=0.000001)
        
    def test_get_height(self):
        # m=1+1*cos(M2*t)
        # 0 < m < 2
        m=Model([H.M0,H.M2])
        m.amplitudes_cos[0]=1
        m.amplitudes_sin[0]=0
        m.amplitudes_cos[1]=1
        m.amplitudes_sin[1]=0
        t0=datetime.now(timezone.utc)
        for _h in range(0,24):
            for _m in range(0,60):
                dt=timedelta(hours=_h,minutes=_m)
                h=m.get_height(t0+dt)
                logger.debug(h)
                self.assertGreaterEqual(h,0)
                self.assertLessEqual(h,2)

    def test_get_height_naive(self):
        m=Model_N10()
        t=datetime.now()
        with self.assertRaises(ValueError) as cm:
            m.get_height(t)
        e=cm.exception
        print(e)

    def test_get_hour_naive(self):
        t=datetime.now()
        with self.assertRaises(ValueError) as cm:
            models.get_hour(t)
        e=cm.exception
        print(e)

    def test_save(self):
        model_ref=Model_N3()
        for i in range(0,4):
            model_ref.amplitudes_cos[i]=random.uniform(-2.0,2.0)
            model_ref.amplitudes_sin[i]=random.uniform(-2.0,2.0)
        file=SER_DIR / "test_save.ser"
        models.save(model_ref,file)
        self.assertTrue(file.is_file())

    def test_load(self):
        model_ref=Model_N3()
        for i in range(0,4):
            model_ref.amplitudes_cos[i]=random.uniform(-2.0,2.0)
            model_ref.amplitudes_sin[i]=random.uniform(-2.0,2.0)
        file=SER_DIR / "test_load.ser"
        models.save(model_ref,file)
        model=models.read(file)
        for i in range(0,4):
            self.assertEqual(model.amplitudes_cos[i],model_ref.amplitudes_cos[i])
            self.assertEqual(model.amplitudes_sin[i],model_ref.amplitudes_sin[i])
