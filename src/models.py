# coding: utf-8
"""
This module deals with Darwin/Doodson models, i.e a list of harmonics that predict tide height based on a Fourrier development.
"""

from harmonics import Harmonic
import harmonics as H
from datetime import datetime
import math

class Model:
    """
    This class holds a fixed list of harmonics, and computerized list of amplitudes and phases.
    """

    def __init__(self,harmonics:list[Harmonic]):
        """
        Constructor of Model given its harmonics.
        """
        self.harmonics=harmonics
        self.amplitudes=[float]*len(harmonics)
        self.phases=[float]*len(harmonics)

    def get_harmonics(self):
        return self.harmonics
    
    def get_amplitudes(self):
        """
        Amplitudes in m matching order with harmonics.
        """
        return self.amplitudes
    
    def get_phases(self):
        """
        Phases in ° matching order with harmonics.
        """
        return self.phases
    
    def get_height(self,t:datetime):
        height=0.0
        for n in range(len(self.harmonics)):
            # speed is °/h
            # dt=(t-H.T0) is timedelta
            # dh=dt.days*24+dt.seconds/3600 is hours (float) from H.T0.
            # speed*dh is °
            # phase is °
            dt=t-H.T0
            dh=dt.days*24+dt.seconds/3600
            x=self.harmonics[n].get_speed()*dh + self.phases[n]
            height+=self.amplitudes[n] * math.cos(math.radians(x))
        return height
    
class Model_N3(Model):
    def __init__(self):
        super().__init__([H.M0,H.S0,H.M2,H.S2,H.N2])

class Model_N6(Model):
    def __init__(self):
        super().__init__([H.M0,H.S0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1])

class Model_N10(Model):
    def __init__(self):
        super().__init__([H.M0,H.S0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4])

class Model_N16(Model):
    def __init__(self):
        super().__init__([H.M0,H.S0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4,
                          H.nu2,H.mu2,H._2N2,H.OO1,H.lambda2])

class Model_N24(Model):
    def __init__(self):
        super().__init__([H.M0,H.S0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4,
                          H.nu2,H.mu2,H._2N2,H.OO1,H.lambda2,
                          H.S1,H.M1,H.J1,H.Mm,H.Ssa,H.Sa,H.Msf,H.Mf])

class Model_N32(Model):
    def __init__(self):
        super().__init__([H.M0,H.S0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4,
                          H.nu2,H.mu2,H._2N2,H.OO1,H.lambda2,
                          H.S1,H.M1,H.J1,H.Mm,H.Ssa,H.Sa,H.Msf,H.Mf,
                          H.rau1,H.Q1,H.T2,H.R2,H._2Q1,H.P1,H._2SM2,H.M3])

