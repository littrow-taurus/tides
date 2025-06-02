import logging
logging.basicConfig(encoding='utf-8',level=logging.DEBUG)
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

logger=logging.getLogger(__name__)

class TestModels(unittest.TestCase):
    def test_create_Model(self):
        """
        Test nominal creation of Model.
        """
        Model([H.M0,H.S0,H.M2,H.S2,H.N2])

    def test_create_Model_N3(self):
        m=Model_N3()
        self.assertIn(H.M0,m.get_harmonics()) # 0
        self.assertIn(H.S0,m.get_harmonics()) # 0
        self.assertIn(H.M2,m.get_harmonics()) # 1
        self.assertIn(H.S2,m.get_harmonics()) # 2
        self.assertIn(H.N2,m.get_harmonics()) # 3
        self.assertEqual(len(m.get_harmonics()),5)
        self.assertEqual(len(m.get_amplitudes_cos()),5)
        self.assertEqual(len(m.get_amplitudes_sin()),5)
        
    def test_create_Model_N6(self):
        m=Model_N6()
        self.assertIn(H.M0,m.get_harmonics()) # 0
        self.assertIn(H.S0,m.get_harmonics()) # 0
        self.assertIn(H.M2,m.get_harmonics()) # 1
        self.assertIn(H.S2,m.get_harmonics()) # 2
        self.assertIn(H.N2,m.get_harmonics()) # 3
        self.assertIn(H.K1,m.get_harmonics()) # 4
        self.assertIn(H.M4,m.get_harmonics()) # 5
        self.assertIn(H.O1,m.get_harmonics()) # 6
        self.assertEqual(len(m.get_harmonics()),8)
        self.assertEqual(len(m.get_amplitudes_cos()),8)
        self.assertEqual(len(m.get_amplitudes_sin()),8)
        
    def test_create_Model_N10(self):
        m=Model_N10()
        self.assertIn(H.M0,m.get_harmonics()) # 0
        self.assertIn(H.S0,m.get_harmonics()) # 0
        self.assertIn(H.M2,m.get_harmonics()) # 1
        self.assertIn(H.S2,m.get_harmonics()) # 2
        self.assertIn(H.N2,m.get_harmonics()) # 3
        self.assertIn(H.K1,m.get_harmonics()) # 4
        self.assertIn(H.M4,m.get_harmonics()) # 5
        self.assertIn(H.O1,m.get_harmonics()) # 6
        self.assertIn(H.M6,m.get_harmonics()) # 7
        self.assertIn(H.MK3,m.get_harmonics()) # 8
        self.assertIn(H.S4,m.get_harmonics()) # 9
        self.assertIn(H.MN4,m.get_harmonics()) # 10
        self.assertEqual(len(m.get_harmonics()),12)
        self.assertEqual(len(m.get_amplitudes_cos()),12)
        self.assertEqual(len(m.get_amplitudes_sin()),12)

    def test_create_Model_N16(self):
        m=Model_N16()
        self.assertIn(H.M0,m.get_harmonics()) # 0
        self.assertIn(H.S0,m.get_harmonics()) # 0
        self.assertIn(H.M2,m.get_harmonics()) # 1
        self.assertIn(H.S2,m.get_harmonics()) # 2
        self.assertIn(H.N2,m.get_harmonics()) # 3
        self.assertIn(H.K1,m.get_harmonics()) # 4
        self.assertIn(H.M4,m.get_harmonics()) # 5
        self.assertIn(H.O1,m.get_harmonics()) # 6
        self.assertIn(H.M6,m.get_harmonics()) # 7
        self.assertIn(H.MK3,m.get_harmonics()) # 8
        self.assertIn(H.S4,m.get_harmonics()) # 9
        self.assertIn(H.MN4,m.get_harmonics()) # 10
        self.assertIn(H.nu2,m.get_harmonics()) # 11
        # self.assertIn(H.S6,m.get_harmonics()) # 12
        self.assertIn(H.mu2,m.get_harmonics()) # 13
        self.assertIn(H._2N2,m.get_harmonics()) # 14
        self.assertIn(H.OO1,m.get_harmonics()) # 15
        self.assertIn(H.lambda2,m.get_harmonics()) # 16
        self.assertEqual(len(m.get_harmonics()),17)
        self.assertEqual(len(m.get_amplitudes_cos()),17)
        self.assertEqual(len(m.get_amplitudes_sin()),17)

    def test_create_Model_N24(self):
        m=Model_N24()
        self.assertIn(H.M0,m.get_harmonics()) # 0
        self.assertIn(H.S0,m.get_harmonics()) # 0
        self.assertIn(H.M2,m.get_harmonics()) # 1
        self.assertIn(H.S2,m.get_harmonics()) # 2
        self.assertIn(H.N2,m.get_harmonics()) # 3
        self.assertIn(H.K1,m.get_harmonics()) # 4
        self.assertIn(H.M4,m.get_harmonics()) # 5
        self.assertIn(H.O1,m.get_harmonics()) # 6
        self.assertIn(H.M6,m.get_harmonics()) # 7
        self.assertIn(H.MK3,m.get_harmonics()) # 8
        self.assertIn(H.S4,m.get_harmonics()) # 9
        self.assertIn(H.MN4,m.get_harmonics()) # 10
        self.assertIn(H.nu2,m.get_harmonics()) # 11
        # self.assertIn(H.S6,m.get_harmonics()) # 12
        self.assertIn(H.mu2,m.get_harmonics()) # 13
        self.assertIn(H._2N2,m.get_harmonics()) # 14
        self.assertIn(H.OO1,m.get_harmonics()) # 15
        self.assertIn(H.lambda2,m.get_harmonics()) # 16
        self.assertIn(H.S1,m.get_harmonics()) # 17
        self.assertIn(H.M1,m.get_harmonics()) # 18
        self.assertIn(H.J1,m.get_harmonics()) # 19
        self.assertIn(H.Mm,m.get_harmonics()) # 20
        self.assertIn(H.Ssa,m.get_harmonics()) # 21
        self.assertIn(H.Sa,m.get_harmonics()) # 22
        self.assertIn(H.Msf,m.get_harmonics()) # 23
        self.assertIn(H.Mf,m.get_harmonics()) # 24
        self.assertEqual(len(m.get_harmonics()),25)
        self.assertEqual(len(m.get_amplitudes_cos()),25)
        self.assertEqual(len(m.get_amplitudes_sin()),25)

    def test_create_Model_N32(self):
        m=Model_N32()
        self.assertIn(H.M0,m.get_harmonics()) # 0
        self.assertIn(H.S0,m.get_harmonics()) # 0
        self.assertIn(H.M2,m.get_harmonics()) # 1
        self.assertIn(H.S2,m.get_harmonics()) # 2
        self.assertIn(H.N2,m.get_harmonics()) # 3
        self.assertIn(H.K1,m.get_harmonics()) # 4
        self.assertIn(H.M4,m.get_harmonics()) # 5
        self.assertIn(H.O1,m.get_harmonics()) # 6
        self.assertIn(H.M6,m.get_harmonics()) # 7
        self.assertIn(H.MK3,m.get_harmonics()) # 8
        self.assertIn(H.S4,m.get_harmonics()) # 9
        self.assertIn(H.MN4,m.get_harmonics()) # 10
        self.assertIn(H.nu2,m.get_harmonics()) # 11
        # self.assertIn(H.S6,m.get_harmonics()) # 12
        self.assertIn(H.mu2,m.get_harmonics()) # 13
        self.assertIn(H._2N2,m.get_harmonics()) # 14
        self.assertIn(H.OO1,m.get_harmonics()) # 15
        self.assertIn(H.lambda2,m.get_harmonics()) # 16
        self.assertIn(H.S1,m.get_harmonics()) # 17
        self.assertIn(H.M1,m.get_harmonics()) # 18
        self.assertIn(H.J1,m.get_harmonics()) # 19
        self.assertIn(H.Mm,m.get_harmonics()) # 20
        self.assertIn(H.Ssa,m.get_harmonics()) # 21
        self.assertIn(H.Sa,m.get_harmonics()) # 22
        self.assertIn(H.Msf,m.get_harmonics()) # 23
        self.assertIn(H.Mf,m.get_harmonics()) # 24
        self.assertIn(H.rau1,m.get_harmonics()) # 25
        self.assertIn(H.Q1,m.get_harmonics()) # 26
        self.assertIn(H.T2,m.get_harmonics()) # 27
        self.assertIn(H.R2,m.get_harmonics()) # 28
        self.assertIn(H._2Q1,m.get_harmonics()) # 29
        self.assertIn(H.P1,m.get_harmonics()) # 30
        self.assertIn(H._2SM2,m.get_harmonics()) # 31
        self.assertIn(H.M3,m.get_harmonics()) # 32
        self.assertEqual(len(m.get_harmonics()),33)
        self.assertEqual(len(m.get_amplitudes_cos()),33)
        self.assertEqual(len(m.get_amplitudes_sin()),33)

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
        m.get_amplitudes_cos()[0]=1
        m.get_amplitudes_sin()[0]=0
        m.get_amplitudes_cos()[1]=1
        m.get_amplitudes_sin()[1]=0
        t0=datetime.now(timezone.utc)
        for _h in range(0,24):
            for _m in range(0,60):
                dt=timedelta(hours=_h,minutes=_m)
                h=m.get_height(t0+dt)
                logger.debug(h)
                self.assertGreaterEqual(h,0)
                self.assertLessEqual(h,2)
