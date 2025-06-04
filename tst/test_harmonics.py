import conf_logging
import logging
import unittest
import random
import harmonics
from harmonics import Harmonic
from harmonics import HarmonicException

logger=logging.getLogger(__name__)

class TestHarmonics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(encoding='utf-8',level=logging.DEBUG)

    def test_create_Harmonic(self):
        """
        Test nominal creation of Harmonic.
        """
        d=Harmonic([1,0,0, 1,0,0])
        self.assertEqual(d.n,[1,0,0, 1,0,0])

    def test_Harmonic_len_numbers(self):
        """
        Test HarmonicException raised when array of numbers length different from 6.
        """
        # len=5
        with self.assertRaises(HarmonicException) as cm:
            Harmonic([0,0,0,0,0])
        e=cm.exception
        logger.debug(e)
        # len=7
        with self.assertRaises(HarmonicException) as cm:
            Harmonic([0,0,0,0,0,0,0])
        e=cm.exception
        logger.debug(e)

    def test_Harmonic_values_limits(self):
        """
        Test values are proper intervals: 
        s ≥ 0, −5 ≤ mi < 5
        """
        # s ≥ 0
        with self.assertRaises(HarmonicException) as cm:
            Harmonic([-1,0,0, 0,0,0])
        e=cm.exception
        logger.debug(e)

        # −5 ≤ mi < 5
        with self.assertRaises(HarmonicException):
            Harmonic([0,-6,0, 0,0,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,5,0, 0,0,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,-6, 0,0,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,5, 0,0,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,0, -6,0,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,0, 5,0,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,0, 0,-6,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,0, 0,5,0])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,0, 0,0,-6])
        with self.assertRaises(HarmonicException):
            Harmonic([0,0,0, 0,0,5])

    def test_Harmonic_get_speed(self):
        """
        Checks sample of Harmonic's speeds.
        """
        # 135 655 -> 13.39866°/hr
        d=Harmonic([1,-2,0, 1,0,0])
        self.assertAlmostEqual(d.get_speed(),13.39866,delta=0.00001)
        d=harmonics.get_by_number(int('055555'))
        self.assertAlmostEqual(d.get_speed(),0.0000000,delta=0.00001)
        d=harmonics.get_by_number(int('056554'))
        self.assertAlmostEqual(d.get_speed(),0.0410667,delta=0.00001)
        d=harmonics.get_by_number(int('063655'))
        self.assertAlmostEqual(d.get_speed(),0.4715211,delta=0.00001)
        d=harmonics.get_by_number(int('125755'))
        self.assertAlmostEqual(d.get_speed(),12.8542862,delta=0.00001)
        d=harmonics.get_by_number(int('127555'))
        self.assertAlmostEqual(d.get_speed(),12.9271398,delta=0.00001)
        d=harmonics.get_by_number(int('173655'))
        self.assertAlmostEqual(d.get_speed(),15.5125897,delta=0.00001)

    def test_get_by_digits(self):
        """
        Checks getting Harmonic instance by numbers.
        """
        n0=random.randint(0,3)
        n1=random.randint(0,9)
        n2=random.randint(0,9)
        n3=random.randint(0,9)
        n4=random.randint(0,9)
        n5=random.randint(0,9)
        d=harmonics.get_by_digits(n0,n1,n2,n3,n4,n5)
        self.assertEqual(d.n,[n0,n1-5,n2-5,n3-5,n4-5,n5-5])

    def test_get_by_number(self):
        """
        Checks getting Harmonic instance by string.
        """
        d=harmonics.get_by_number(155555)
        self.assertEqual(d.n,[1,0,0,0,0,0])
        d=harmonics.get_by_number(266444)
        self.assertEqual(d.n,[2,1,1,-1,-1,-1])

    def test_get_by_number_wrong(self):
        """
        Checks getting Harmonic instance by string.
        """
        with self.assertRaises(HarmonicException) as cm:
            harmonics.get_by_number(-1)
        e=cm.exception
        logger.debug(e)

    def test_dtau(self):
        logger.debug(harmonics.dtau)
        self.assertAlmostEqual(harmonics.dtau,360/(1.035*24),delta=harmonics.dtau/10000) # period 1.035 days (precision 0.01%)

    def test_ds(self):
        logger.debug(harmonics.ds)
        self.assertAlmostEqual(harmonics.ds,360/(27.321582*24),delta=harmonics.ds/10000) # period 27.321582 days (precision 0.01%)
        
    def test_dh(self):
        logger.debug(harmonics.dh)
        self.assertAlmostEqual(harmonics.dh,360/(365.242199*24),delta=harmonics.dh/10000) # period 365.242199 days (precision 0.01%)
        
    def test_dp(self):
        logger.debug(harmonics.dp)
        self.assertAlmostEqual(harmonics.dp,360/(8.847*365.242199*24),delta=harmonics.dp/10000) # period 8.847 years (precision 0.01%)
        
    def test_dN(self):
        logger.debug(harmonics.dN)
        self.assertAlmostEqual(harmonics.dN,360/(18.611*365.242199*24),delta=harmonics.dN/10000) # period 18.611 years (precision 0.01%)
        
    def test_dp1(self):
        logger.debug(harmonics.dp1)
        if not harmonics.APPLY_TIME_CORRECTION:
            self.assertAlmostEqual(harmonics.dp1,360/(20940*365.242199*24),delta=harmonics.dp1/10000) # period 20940 years (precision 0.01%)
        else:
            self.assertAlmostEqual(harmonics.dp1,360/(20925*365.242199*24),delta=harmonics.dp1/10000) # period 20940 years (precision 0.01%)

    def test_constants(self):
        # Long period tides
        # M0    055 555 0.0000000 (1)(3)
        self.assertAlmostEqual(harmonics.M0.get_speed(),0.0000000,delta=0.0000010)
        # S0    055 555 0.0000000 (1)(3)
        self.assertAlmostEqual(harmonics.S0.get_speed(),0.0000000,delta=0.0000010)
        # Sa    056 554 0.0410667 (1)(2 difference)
        self.assertAlmostEqual(harmonics.Sa.get_speed(),0.0410667,delta=0.0000010)
        # Ssa   057 555 0.0821373 (1)(2)(3)
        self.assertAlmostEqual(harmonics.Ssa.get_speed(),0.0821373,delta=0.0000010)
        # Sta   058 554 0.1232040 (1)
        self.assertAlmostEqual(harmonics.Sta.get_speed(),0.1232040,delta=0.0000010)
        # Msm   063 655 0.4715211 (1)
        self.assertAlmostEqual(harmonics.Msm.get_speed(),0.4715211,delta=0.0000010)
        # Mm    065 455 0.5443747 (1)(2)(3)
        self.assertAlmostEqual(harmonics.Mm.get_speed(),0.5443747,delta=0.0000010)
        # Msf   073 555 1.0158958 (1)(2)
        self.assertAlmostEqual(harmonics.Msf.get_speed(),1.0158958,delta=0.0000010)
        # Mf    075 555 1.0980331 (1)(2)(3)
        self.assertAlmostEqual(harmonics.Mf.get_speed(),1.0980331,delta=0.0000010)
        # Mstm  083 655 1.5695548 (1)
        self.assertAlmostEqual(harmonics.Mstm.get_speed(),1.5695548,delta=0.0000010)
        # Mtm   085 455 1.6424078 (1)
        self.assertAlmostEqual(harmonics.Mtm.get_speed(),1.6424078,delta=0.0000010)
        # Msqm  093 555 2.1139288 (1)
        self.assertAlmostEqual(harmonics.Msqm.get_speed(),2.1139288,delta=0.0000010)
        # nodal_M0_1    055 565 0.0022067 (3)
        self.assertAlmostEqual(harmonics.nodal_M0_1.get_speed(),0.0022067,delta=0.0000010)
        # nodal_M0_2    075 565 1.10024 (3)
        self.assertAlmostEqual(harmonics.nodal_M0_2.get_speed(),1.10024,delta=0.0000010)

        # Diurnal tides
        # 2Q1   125 755 12.8542862 (1)(2)
        self.assertAlmostEqual(harmonics._2Q1.get_speed(),12.8542862,delta=0.0000010)
        # sigma1 	127 555 12.9271398 (1)
        self.assertAlmostEqual(harmonics.sigma1.get_speed(),12.9271398,delta=0.0000010)
        # Q1    135 655 13.3986609 (1)(2)
        self.assertAlmostEqual(harmonics.Q1.get_speed(),13.3986609,delta=0.0000010)
        # rau1 	137 455 13.4715145 (1)(2 différence)
        self.assertAlmostEqual(harmonics.rau1.get_speed(),13.4715145,delta=0.0000010)
        # O1    145 555 13.9430356 (1)(2)(3)
        self.assertAlmostEqual(harmonics.O1.get_speed(),13.9430356,delta=0.0000010)
        # tau1 	147 555 14.0251729 (1)
        self.assertAlmostEqual(harmonics.tau1.get_speed(),14.0251729,delta=0.0000010)
        # khi1 	157 455 14.5695476 (1)
        self.assertAlmostEqual(harmonics.khi1.get_speed(),14.5695476,delta=0.0000010)
        # pi1 	162 556 14.9178647 (1)
        self.assertAlmostEqual(harmonics.pi1.get_speed(),14.9178647,delta=0.0000010)
        # P1    163 555 14.9589314 (1)(2)(3)
        self.assertAlmostEqual(harmonics.P1.get_speed(),14.9589314,delta=0.0000010)
        # K1    165 555 15.0410686 (2)(3)
        self.assertAlmostEqual(harmonics.K1.get_speed(),15.0410686,delta=0.0000010)
        # psi1 	166 554 15.0821353 (1)
        self.assertAlmostEqual(harmonics.psi1.get_speed(),15.0821353,delta=0.0000010)
        # phi1 	167 555 15.1232059 (1)
        self.assertAlmostEqual(harmonics.phi1.get_speed(),15.1232059,delta=0.0000010)
        # teta1 	173 655 15.5125897 (1)
        self.assertAlmostEqual(harmonics.teta1.get_speed(),15.5125897,delta=0.0000010)     
        # J1    175 455 15.5854433 (1)(2)
        self.assertAlmostEqual(harmonics.J1.get_speed(),15.5854433,delta=0.0000010)
        # OO1   185 555 16.1391017 (1)(2)
        self.assertAlmostEqual(harmonics.OO1.get_speed(),16.1391017,delta=0.0000010)
        # nu1 	195 455 16.6834764 (1)
        self.assertAlmostEqual(harmonics.nu1.get_speed(),16.6834764,delta=0.0000010)
        # S1    164 555 15.0000000 (2)
        self.assertAlmostEqual(harmonics.S1.get_speed(),15.0000000,delta=0.0000010)
        # M1    155 555 14.4920521 (2)
        self.assertAlmostEqual(harmonics.M1.get_speed(),14.4920521,delta=0.0000010)

        # Semi-diurnal tides
        # 2N2   235 755 27.8953548 (1)(2)
        self.assertAlmostEqual(harmonics._2N2.get_speed(),27.8953548,delta=0.0000010)
        # mu2 	237 555 27.9682084 (1)(2)
        self.assertAlmostEqual(harmonics.mu2.get_speed(),27.9682084,delta=0.0000010)
        # N2    245 655 28.4397295 (1)(2)(3)
        self.assertAlmostEqual(harmonics.N2.get_speed(),28.4397295,delta=0.0000010)
        # nu2 	247 455 28.512583 (1)(2)
        self.assertAlmostEqual(harmonics.nu2.get_speed(),28.512583,delta=0.0000010)
        # M2    255 555 28.9841042 (1)(2)(3)
        self.assertAlmostEqual(harmonics.M2.get_speed(),28.9841042,delta=0.0000010)
        # lambda2 	263 655 29.4556253 (1)(2)
        self.assertAlmostEqual(harmonics.lambda2.get_speed(),29.4556253,delta=0.0000010)
        # L2    265 455 29.5284789 (1)(2)
        self.assertAlmostEqual(harmonics.L2.get_speed(),29.5284789,delta=0.0000010)
        # T2    272 556 29.9589333 (1)(2)
        self.assertAlmostEqual(harmonics.T2.get_speed(),29.9589333,delta=0.0000010)
        # S2    273 555 30.0000000 (1)(2)(3)
        self.assertAlmostEqual(harmonics.S2.get_speed(),30.0000000,delta=0.0000010)
        # R2    274 554 30.0410667 (1)(2 difference)
        self.assertAlmostEqual(harmonics.R2.get_speed(),30.0410667,delta=0.0000010)
        # K2    275 555 30.0821373 (2)(3)
        self.assertAlmostEqual(harmonics.K2.get_speed(),30.0821373,delta=0.0000010)
        # 2SM2  291.555 31.0158958 (2)
        self.assertAlmostEqual(harmonics._2SM2.get_speed(),31.0158958,delta=0.0000010)

        # Short period tides
        # M4    455 555 57.9682084 (2)
        self.assertAlmostEqual(harmonics.M4.get_speed(),57.9682084,delta=0.0000010)
        # M6    655 555 86.9523127 (2)
        self.assertAlmostEqual(harmonics.M6.get_speed(),86.9523127,delta=0.0000010)
        # MK3   365 555 44.0251729 (2)
        self.assertAlmostEqual(harmonics.MK3.get_speed(),44.0251729,delta=0.0000010)
        # S4    491 555 60.0000000 (2)
        self.assertAlmostEqual(harmonics.S4.get_speed(),60.0000000,delta=0.0000010)
        # MN4   445 655 57.4238337 (2)
        self.assertAlmostEqual(harmonics.MN4.get_speed(),57.42383374,delta=0.0000010)
        # M3    355 555 43.4761563 (2)
        self.assertAlmostEqual(harmonics.M3.get_speed(),43.4761563,delta=0.0000010)
        # 2MK3  345 555 42.9271398 (2)
        self.assertAlmostEqual(harmonics._2MK3.get_speed(),42.9271398,delta=0.0000010)
        # M8    855 555 115.9364166 (2)
        self.assertAlmostEqual(harmonics.M8.get_speed(),115.9364166,delta=0.0000010)
        # MS4   473 555 58.9841042 (2)
        self.assertAlmostEqual(harmonics.MS4.get_speed(),58.9841042,delta=0.0000010)

        # (1): Source [Chapitre 4 Le potentiel générateur des marées](http://fabien.lefevre.free.fr/These_HTML/doc0004.htm)
        # (2): Source [Theory of tides - Wikipedia](https://en.wikipedia.org/wiki/Theory_of_tides)
        # (3): Source [Lecture 1: Introduction to ocean tides, Myrl Hendershott](https://www.whoi.edu/cms/files/lecture01_21351.pdf)
