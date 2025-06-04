# coding: utf-8
"""
This module deals with Darwin/Doodson models, i.e a list of harmonics that predict tide height based on a Fourrier development.
"""

import conf_logging
import logging
from harmonics import Harmonic
import harmonics as H
from datetime import datetime
import math
from deprecated import deprecated
from harmonics import HarmonicException
from datas import Data
import numpy
from pathlib import Path
import pickle

logger=logging.getLogger(__name__)

class Model:
    """
    This class holds a fixed list of harmonics, and computerized list of amplitudes (cosinus ans sinus).

    :param harmonics: List of Harmonic that makes the model.
    :type harmonics: list[Harmonic]
    :param amplitudes_cos: List of consinus amplitudes using same order as harmonics list.
    :type amplitudes_cos: list[float]
    :param amplitudes_sin: List of consinus amplitudes using same order as harmonics list.
    :type amplitudes_sin: list[float]
    """

    def __init__(self,harmonics:list[Harmonic],min_delta=0.5):
        """
        Constructor of Model given its harmonics. Amplitudes are initialy zeroed.

        :param harmonics: List of Harmonic that makes the model.
        :type harmonics: list[Harmonic]
        :param harmonics: The list of harmonics to check if they are separated enough.
        :type harmonics: list[Harmonic]
        :param min_delta: Minimum space between two harmonics (°/h)
        :type min_delta: float
        """
        self.harmonics=harmonics
        check_harmonics(harmonics,min_delta)
        self.amplitudes_cos=[float]*len(harmonics)
        self.amplitudes_sin=[float]*len(harmonics)

    @deprecated(version='0.0.4', reason="Use direct access to attribute.")
    def get_harmonics(self):
        return self.harmonics
    
    @deprecated(version='0.0.4', reason="Use direct access to attribute.")
    def get_amplitudes_cos(self):
        """
        Amplitudes of cosinus in m matching order with harmonics.
        """
        return self.amplitudes_cos
    
    @deprecated(version='0.0.4', reason="Use direct access to attribute.")
    def get_amplitudes_sin(self):
        """
        Amplitudes of sinus in m matching order with harmonics.
        """
        return self.amplitudes_sin
    
    def get_height(self,t:datetime):
        """
        Computes height with this model for time passed as parameter.  
        h=Ʃ Ac(i) * cos(w(i)*dh) + As(i) * sin(w(i)*dh)
        where w: rotation speed (°/h)

        :param t: We estimate tide's height at this time with the model.
        :type datetime: MUST be aware (oposite to naive).
        """
        height=0.0
        for n in range(len(self.harmonics)):
            # speed is °/h
            # dh is h
            # speed*dh is °
            dh=get_hour(t) # time from T0 in hours 
            angle=math.radians(self.harmonics[n].get_speed()*dh)
            height+=self.amplitudes_cos[n] * math.cos(angle) + self.amplitudes_sin[n] * math.sin(angle)
        return height
    
class Model_N3(Model):
    """
    Model N3 (3 harmonics with a non nul frequency): (M0), M2, S2, N2.
    """
    def __init__(self):
        super().__init__([H.M0,H.M2,H.S2,H.N2])

class Model_N6(Model):
    """
    Model N6 (6 harmonics with a non nul frequency): (M0), M2, S2, N2, K1, M4, O1.
    """
    def __init__(self):
        super().__init__([H.M0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1])

class Model_N10(Model):
    """
    Model N10 (10 harmonics with a non nul frequency): (M0), M2, S2, N2, K1, M4, O1, M6, MK3, S4, MN4.
    """
    def __init__(self):
        super().__init__([H.M0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4])

class Model_N16(Model):
    """
    Model N16 (16 harmonics with a non nul frequency): (M0), M2, S2, N2, K1, M4, O1, M6, MK3, S4, MN4, mu2, _2N2, OO1, lambda2.
    """
    def __init__(self):
        super().__init__([H.M0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4,
                          H.nu2,H.mu2,H._2N2,H.OO1,H.lambda2],min_delta=0.05)

class Model_N24(Model):
    """
    Model N24 (24 harmonics with a non nul frequency): (M0), M2, S2, N2, K1, M4, O1, M6, MK3, S4, MN4, nu2, mu2, _2N2, OO1, lambda2, S1, M1, J1, Mm, Ssa, Sa, Msf, Mf.
    """
    def __init__(self):
        super().__init__([H.M0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4,
                          H.nu2,H.mu2,H._2N2,H.OO1,H.lambda2,
                          H.S1,H.M1,H.J1,H.Mm,H.Ssa,H.Sa,H.Msf,H.Mf],min_delta=0.04)

class Model_N32(Model):
    """
    Model N32 (32 harmonics with a non nul frequency): (M0), M2, S2, N2, K1, M4, O1, M6, MK3, S4, MN4, nu2, mu2, _2N2, OO1, lambda2, S1, M1, J1, Mm, Ssa, Sa, Msf, Mf,  rau1, Q1, T2, R2, _2Q1, P1, _2SM2, M3.
    """
    def __init__(self):
        super().__init__([H.M0,H.M2,H.S2,H.N2,
                          H.K1,H.M4,H.O1,
                          H.M6,H.MK3,H.S4,H.MN4,
                          H.nu2,H.mu2,H._2N2,H.OO1,H.lambda2,
                          H.S1,H.M1,H.J1,H.Mm,H.Ssa,H.Sa,H.Msf,H.Mf,
                          H.rau1,H.Q1,H.T2,H.R2,H._2Q1,H.P1,H._2SM2,H.M3],min_delta=0.03)
        
class ModelError():
    """
    This class holds datas resulting in measurement comparing a model and a set of datas.

    :param p: List of percentiles of absolutes error. Each element of the list is a tuple. This tuple contains the percentile, and the value (ex: p30=0.25 -> (30,0.25)) 
    :type p: list[tuple(int,float)]

    :param mean: Mean error
    :type mean: float
    :param min: Minimal derivation model error (negative value)
    :type min: float
    :param max: Maximal derivation model error (positive value)
    :type max: float
    :param var: Variance of errors.
    :type var: float
    :param abs: Absolute error
    :type abs: float
    """
    def __init__(self,model:Model,data_list:list[Data]):
        """
        Constructor of the model's error measurment. It computes all errors (measures) data.

        :param model: Model to measure
        :type model: Model
        :param data_list: Reference datas the model is tested against
        :type data_list: list[Data]
        """
        delta_list=[]
        for data in data_list:
            height_ref=data.height
            height_mod=model.get_height(data.t)
            delta=height_mod-height_ref
            delta_list.append(delta)

        abs_delta_list=numpy.absolute(delta_list)
        self.p=[]
        for perc in range(10,100,10):
            self.p.append((perc,numpy.percentile(abs_delta_list,perc))) # tuple
        self.mean=numpy.mean(delta_list)
        self.min=numpy.min(delta_list)
        self.max=numpy.max(delta_list)
        self.var=numpy.var(delta_list)
        self.abs=numpy.mean(abs_delta_list)

    def __str__(self):
        p_str=""
        for p in self.p:
            p_str+=f"\np{p[0]}: {p[1]:0.4f}"
        return f"mean: {self.mean:0.4f}, min: {self.min:0.4f}, max: {self.max:0.4f}, var: {self.var:0.4f}, abs: {self.abs:0.4f}{p_str}"

def get_hour(t:datetime)->float:
    """
    Computes the number of hours (float) elapsed from H.T0.

    :param t: Time to convert to time relative to T0.
    :type datetime: MUST be aware (oposite to naive).
    :return: Number of hours (decimal) eplapsed from T0 to t.
    :rtype: float.
    """
    if t.tzinfo is None:
        raise ValueError("t is not datetime aware")
    # dt=(t-H.T0) is timedelta
    # dh=dt.days*24+dt.seconds/3600 is hours (float) from H.T0.
    dt=t-H.T0
    dh=dt.days*24+dt.seconds/3600
    return dh

def check_harmonics(harmonics:list[Harmonic],min_delta=0.5):
    """
    Checks there is no harmonics too close each other.

    Theoric minimum difference of frequency between 2 harmonic frequencies is fs/N  
    where fs: sampling frequency
    and N: number of samples

    As we don't know before we compute the model how many samples we will use for estimation, we don't know N. So we decide a limit for N, and also decide a fs, both arbitrary.
    We consider we systematically compute models using several days of data (lets say minimum 30 days). For fs, we shall sample at least every 15mn minimum.  
    N > 30*24*4 samples
    fs > 1/15mn (or pulsation 360°/15mn=1440°/h)
    So differences between two harmonic speeds (pulsation) is 1440/30/24/4=0.5°/h

    As all of this is pure speculation, we allow to pass a min_delta.

    :param harmonics: The list of harmonics to check if they are separated enough.
    :type harmonics: list[Harmonic]
    :param min_delta: Minimum space between two harmonics (°/h)
    :type min_delta: float
    """
    for i in range(len(harmonics)):
        for j in range(len(harmonics)):
            if i < j:
                delta=math.fabs(harmonics[i].get_speed()-harmonics[j].get_speed())
                if delta < min_delta:
                    raise HarmonicException(f"Harmonics are too close to each other: {i}:{harmonics[i].get_speed()}, {j}:{harmonics[j].get_speed()} (delta={delta})")
                
def save(model:Model,file:Path):
    """
    Saves (serialize) the model in a file.

    :param model: The model to save. 
    :type model: Model
    :param file: The destination file where model is serialized.
    :type file: Path
    """
    f=open(file,"wb")
    pickle.dump(model,f,protocol=pickle.DEFAULT_PROTOCOL)
    f.close()

def read(file:Path) -> Model:
    """
    Loads (deserialize) the model from a file.

    :param file: The serialization file from where model is read.
    :type file: Path
    :return model: The model to restore. 
    :rtype: Model
    """
    f=open(file,"rb")
    model=pickle.load(f)
    f.close()
    return model
