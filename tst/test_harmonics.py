import logging
logging.basicConfig(encoding='utf-8',level=logging.DEBUG)
import unittest
import random
import harmonics
from harmonics import Doodson
from harmonics import DoodsonException

logger=logging.getLogger(__name__)

class TestHarmonics(unittest.TestCase):
    def test_create_Doodson(self):
        """
        Test nominal creation of Doodson.
        """
        d=Doodson([1,0,0, 1,0,0])
        self.assertEqual(d.n,[1,0,0, 1,0,0])

    def test_Doodson_len_numbers(self):
        """
        Test DoodsonException raised when array of numbers length different from 6.
        """
        # len=5
        with self.assertRaises(DoodsonException) as cm:
            Doodson([0,0,0,0,0])
        e=cm.exception
        print(e)
        # len=7
        with self.assertRaises(DoodsonException) as cm:
            Doodson([0,0,0,0,0,0,0])
        e=cm.exception
        print(e)

    def test_Doodson_values(self):
        """
        Test values are proper intervals: 
        s ≥ 0, −5 ≤ mi < 5
        """
        # s ≥ 0
        with self.assertRaises(DoodsonException) as cm:
            Doodson([-1,0,0, 0,0,0])
        e=cm.exception
        print(e)

        # −5 ≤ mi < 5
        with self.assertRaises(DoodsonException):
            Doodson([0,-6,0, 0,0,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,5,0, 0,0,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,-6, 0,0,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,5, 0,0,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,0, -6,0,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,0, 5,0,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,0, 0,-6,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,0, 0,5,0])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,0, 0,0,-6])
        with self.assertRaises(DoodsonException):
            Doodson([0,0,0, 0,0,5])

    def test_Doodson_get_frequency(self):
        """
        Checks sample of Doodson's frequencies.
        """
        # 135 655 -> 13.39866°/hr
        d=Doodson([1,-2,0, 1,0,0])
        self.assertAlmostEqual(d.get_frequency(),13.39866,delta=0.00001)

    def test_get_by_digits(self):
        """
        Checks getting Doodson instance by numbers.
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
        Checks getting Doodson instance by string.
        """
        d=harmonics.get_by_number(155555)
        self.assertEqual(d.n,[1,0,0,0,0,0])
        d=harmonics.get_by_number(266444)
        self.assertEqual(d.n,[2,1,1,-1,-1,-1])

    def test_get_by_number_wrong(self):
        """
        Checks getting Doodson instance by string.
        """
        with self.assertRaises(DoodsonException) as cm:
            harmonics.get_by_number(-1)
        e=cm.exception
        print(e)

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

        