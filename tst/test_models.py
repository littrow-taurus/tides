import unittest
from models import Model
from models import Model_N3
from models import Model_N6
from models import Model_N10
from models import Model_N16
from models import Model_N24
from models import Model_N32
import harmonics

class TestModels(unittest.TestCase):
    def test_create_Model(self):
        """
        Test nominal creation of Model.
        """
        Model([harmonics.M0,harmonics.S0,harmonics.M2,harmonics.S2,harmonics.N2])

    def test_create_Model_N3(self):
        m=Model_N3()
        self.assertIn(harmonics.M0,m.get_harmonics()) # 0
        self.assertIn(harmonics.S0,m.get_harmonics()) # 0
        self.assertIn(harmonics.M2,m.get_harmonics()) # 1
        self.assertIn(harmonics.S2,m.get_harmonics()) # 2
        self.assertIn(harmonics.N2,m.get_harmonics()) # 3
        self.assertEqual(len(m.get_harmonics()),5)
        self.assertEqual(len(m.get_amplitudes()),5)
        self.assertEqual(len(m.get_phases()),5)
        
    def test_create_Model_N6(self):
        m=Model_N6()
        self.assertIn(harmonics.M0,m.get_harmonics()) # 0
        self.assertIn(harmonics.S0,m.get_harmonics()) # 0
        self.assertIn(harmonics.M2,m.get_harmonics()) # 1
        self.assertIn(harmonics.S2,m.get_harmonics()) # 2
        self.assertIn(harmonics.N2,m.get_harmonics()) # 3
        self.assertIn(harmonics.K1,m.get_harmonics()) # 4
        self.assertIn(harmonics.M4,m.get_harmonics()) # 5
        self.assertIn(harmonics.O1,m.get_harmonics()) # 6
        self.assertEqual(len(m.get_harmonics()),8)
        self.assertEqual(len(m.get_amplitudes()),8)
        self.assertEqual(len(m.get_phases()),8)
        
    def test_create_Model_N10(self):
        m=Model_N10()
        self.assertIn(harmonics.M0,m.get_harmonics()) # 0
        self.assertIn(harmonics.S0,m.get_harmonics()) # 0
        self.assertIn(harmonics.M2,m.get_harmonics()) # 1
        self.assertIn(harmonics.S2,m.get_harmonics()) # 2
        self.assertIn(harmonics.N2,m.get_harmonics()) # 3
        self.assertIn(harmonics.K1,m.get_harmonics()) # 4
        self.assertIn(harmonics.M4,m.get_harmonics()) # 5
        self.assertIn(harmonics.O1,m.get_harmonics()) # 6
        self.assertIn(harmonics.M6,m.get_harmonics()) # 7
        self.assertIn(harmonics.MK3,m.get_harmonics()) # 8
        self.assertIn(harmonics.S4,m.get_harmonics()) # 9
        self.assertIn(harmonics.MN4,m.get_harmonics()) # 10
        self.assertEqual(len(m.get_harmonics()),12)
        self.assertEqual(len(m.get_amplitudes()),12)
        self.assertEqual(len(m.get_phases()),12)

    def test_create_Model_N16(self):
        m=Model_N16()
        self.assertIn(harmonics.M0,m.get_harmonics()) # 0
        self.assertIn(harmonics.S0,m.get_harmonics()) # 0
        self.assertIn(harmonics.M2,m.get_harmonics()) # 1
        self.assertIn(harmonics.S2,m.get_harmonics()) # 2
        self.assertIn(harmonics.N2,m.get_harmonics()) # 3
        self.assertIn(harmonics.K1,m.get_harmonics()) # 4
        self.assertIn(harmonics.M4,m.get_harmonics()) # 5
        self.assertIn(harmonics.O1,m.get_harmonics()) # 6
        self.assertIn(harmonics.M6,m.get_harmonics()) # 7
        self.assertIn(harmonics.MK3,m.get_harmonics()) # 8
        self.assertIn(harmonics.S4,m.get_harmonics()) # 9
        self.assertIn(harmonics.MN4,m.get_harmonics()) # 10
        self.assertIn(harmonics.nu2,m.get_harmonics()) # 11
        # self.assertIn(harmonics.S6,m.get_harmonics()) # 12
        self.assertIn(harmonics.mu2,m.get_harmonics()) # 13
        self.assertIn(harmonics._2N2,m.get_harmonics()) # 14
        self.assertIn(harmonics.OO1,m.get_harmonics()) # 15
        self.assertIn(harmonics.lambda2,m.get_harmonics()) # 16
        self.assertEqual(len(m.get_harmonics()),17)
        self.assertEqual(len(m.get_amplitudes()),17)
        self.assertEqual(len(m.get_phases()),17)

    def test_create_Model_N24(self):
        m=Model_N24()
        self.assertIn(harmonics.M0,m.get_harmonics()) # 0
        self.assertIn(harmonics.S0,m.get_harmonics()) # 0
        self.assertIn(harmonics.M2,m.get_harmonics()) # 1
        self.assertIn(harmonics.S2,m.get_harmonics()) # 2
        self.assertIn(harmonics.N2,m.get_harmonics()) # 3
        self.assertIn(harmonics.K1,m.get_harmonics()) # 4
        self.assertIn(harmonics.M4,m.get_harmonics()) # 5
        self.assertIn(harmonics.O1,m.get_harmonics()) # 6
        self.assertIn(harmonics.M6,m.get_harmonics()) # 7
        self.assertIn(harmonics.MK3,m.get_harmonics()) # 8
        self.assertIn(harmonics.S4,m.get_harmonics()) # 9
        self.assertIn(harmonics.MN4,m.get_harmonics()) # 10
        self.assertIn(harmonics.nu2,m.get_harmonics()) # 11
        # self.assertIn(harmonics.S6,m.get_harmonics()) # 12
        self.assertIn(harmonics.mu2,m.get_harmonics()) # 13
        self.assertIn(harmonics._2N2,m.get_harmonics()) # 14
        self.assertIn(harmonics.OO1,m.get_harmonics()) # 15
        self.assertIn(harmonics.lambda2,m.get_harmonics()) # 16
        self.assertIn(harmonics.S1,m.get_harmonics()) # 17
        self.assertIn(harmonics.M1,m.get_harmonics()) # 18
        self.assertIn(harmonics.J1,m.get_harmonics()) # 19
        self.assertIn(harmonics.Mm,m.get_harmonics()) # 20
        self.assertIn(harmonics.Ssa,m.get_harmonics()) # 21
        self.assertIn(harmonics.Sa,m.get_harmonics()) # 22
        self.assertIn(harmonics.Msf,m.get_harmonics()) # 23
        self.assertIn(harmonics.Mf,m.get_harmonics()) # 24
        self.assertEqual(len(m.get_harmonics()),25)
        self.assertEqual(len(m.get_amplitudes()),25)
        self.assertEqual(len(m.get_phases()),25)

    def test_create_Model_N32(self):
        m=Model_N32()
        self.assertIn(harmonics.M0,m.get_harmonics()) # 0
        self.assertIn(harmonics.S0,m.get_harmonics()) # 0
        self.assertIn(harmonics.M2,m.get_harmonics()) # 1
        self.assertIn(harmonics.S2,m.get_harmonics()) # 2
        self.assertIn(harmonics.N2,m.get_harmonics()) # 3
        self.assertIn(harmonics.K1,m.get_harmonics()) # 4
        self.assertIn(harmonics.M4,m.get_harmonics()) # 5
        self.assertIn(harmonics.O1,m.get_harmonics()) # 6
        self.assertIn(harmonics.M6,m.get_harmonics()) # 7
        self.assertIn(harmonics.MK3,m.get_harmonics()) # 8
        self.assertIn(harmonics.S4,m.get_harmonics()) # 9
        self.assertIn(harmonics.MN4,m.get_harmonics()) # 10
        self.assertIn(harmonics.nu2,m.get_harmonics()) # 11
        # self.assertIn(harmonics.S6,m.get_harmonics()) # 12
        self.assertIn(harmonics.mu2,m.get_harmonics()) # 13
        self.assertIn(harmonics._2N2,m.get_harmonics()) # 14
        self.assertIn(harmonics.OO1,m.get_harmonics()) # 15
        self.assertIn(harmonics.lambda2,m.get_harmonics()) # 16
        self.assertIn(harmonics.S1,m.get_harmonics()) # 17
        self.assertIn(harmonics.M1,m.get_harmonics()) # 18
        self.assertIn(harmonics.J1,m.get_harmonics()) # 19
        self.assertIn(harmonics.Mm,m.get_harmonics()) # 20
        self.assertIn(harmonics.Ssa,m.get_harmonics()) # 21
        self.assertIn(harmonics.Sa,m.get_harmonics()) # 22
        self.assertIn(harmonics.Msf,m.get_harmonics()) # 23
        self.assertIn(harmonics.Mf,m.get_harmonics()) # 24
        self.assertIn(harmonics.rau1,m.get_harmonics()) # 25
        self.assertIn(harmonics.Q1,m.get_harmonics()) # 26
        self.assertIn(harmonics.T2,m.get_harmonics()) # 27
        self.assertIn(harmonics.R2,m.get_harmonics()) # 28
        self.assertIn(harmonics._2Q1,m.get_harmonics()) # 29
        self.assertIn(harmonics.P1,m.get_harmonics()) # 30
        self.assertIn(harmonics._2SM2,m.get_harmonics()) # 31
        self.assertIn(harmonics.M3,m.get_harmonics()) # 32
        self.assertEqual(len(m.get_harmonics()),33)
        self.assertEqual(len(m.get_amplitudes()),33)
        self.assertEqual(len(m.get_phases()),33)
