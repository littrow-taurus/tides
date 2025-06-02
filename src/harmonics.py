# coding: utf-8
"""
This module contains all that deals with harmonics used by Darwin/Doodle models.

The Doodson arguments are:
tau = 15°*t + h - s, mean Lunar time, the Greenwich hour angle of the mean Moon plus 12 hours.  
s = 277.0248 + 481267.8906*T + 0.0020*T^2 + ..., mean longitude of the Moon.  
h = 280.1895 + 36000.7689*T + 0.0003*T^2 + ..., mean longitude of the Sun.  
p = 334.3853 + 4069.0340*T — 0.0103*T^2 + ..., longitude of the Moon's mean perigee.  
N = 100.8432 + 1934.420*T — 0.0021*T^2 + ..., negative of the longitude of the Moon's mean ascending node on the ecliptic.  
P1 = 281.2209 + 1.7192*T + 0.0005*T^2 + ..., longitude of the Sun's mean perigee.  
where T is a Julian century of 36,525 mean solar days (start 1899-12-31=T0). So T=t/36525*24 if t is hours.

For example, lets see s, and how to compute s speed ds/dt.  
s = 277.0248 + 481267.8906*(t/36525*24) + 0.0020*(t/36525*24)^2 + ..., where t is time in hours from T0.  
ds/dt = 481267.8906/(36525*24) + 0.0020*2*(t/36525*24)
ds/dt = (481267.8906+2*0.0020*t)/36525*24

tau=15°*t+h-s  
dtau/dt=15+dh/dt-ds/dt  

In the program variables such as ds/dt are called ds.
"""

import logging
import datetime
from datetime import datetime
from datetime import timezone

logger=logging.getLogger(__name__)

APPLY_TIME_CORRECTION=True
"Boolean that apply time correction in T^2 or not."

T0=datetime(1900,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
"All times origin for whole program."

_t=0
if APPLY_TIME_CORRECTION:
    # As we compute number of ceturies, we don't care about seconds which materilizes a fraction of day
    _t=(datetime.now(timezone.utc)-T0).days/36525

ds=(481267.8906+2*0.0020*_t)/36525/24
"Speed of longitude of the Moon (°/h)."
dh=(36000.7689+2*0.0003*_t)/36525/24
"Speed of longitude of the Sun (°/h)."
dp=(4069.0340+2*0.0103*_t)/36525/24
"Speed of longitude of the Moon's mean perigee (°/h)."
dN=(1934.420+2*0.0021*_t)/36525/24
"Negative speed of longitude of the Moon's mean ascending node on the ecliptic (°/h)."
dp1=(1.71920+2*0.0005*_t)/36525/24
"Speed of longitude of the Sun's mean perigee (°/h)."
dtau=15+dh-ds
"Speed of moon (°/h)."

class HarmonicException(Exception):
    pass

class Harmonic:
    """
    Holds an harmonic based on its Doodson numbers.

    Documentation
    -------------
    # Doodson numbers
    For convenience, the frequencies σj may be written as  
    Doodson number = s mj1 mj2 mj3 mj4 mj5 + 0 5 5 5 5 5,  
    where the addition of 055555 is simply so that the Doodson numbers are all positive (since in general the mji lie in the range −5 ≤ mji < 5). 
    The Doodson numbers are also given in table 2.

    | Period                    | Nomenclature                     |
    | ------------------------- | -------------------------------- |
    | 360◦/ω1 = 27.321582 days  | period of lunar declination      |
    | 360◦/ω2 = 365.242199 days | period of solar declination      |
    | 360◦/ω3 = 8.847 years     | period of lunar perigee rotation |
    | 360◦/ω4 = 18.613 years    | period of lunar node rotation    |
    | 360◦/ω5 = 20940 years     | period of perihelion rotation    |

    - [Lecture 1: Introduction to ocean tides, Myrl Hendershott](https://www.whoi.edu/cms/files/lecture01_21351.pdf)
    - [Transformation between the International Terrestrial Reference System and the Geocentric Celestial Reference System](https://iers-conventions.obspm.fr/content/chapter5/icc5.pdf)
    """

    def __init__(self,n:list[int]):
        """
        Constructor.
        
        Parameters
        ----------
        n: list
            Array of the 6 harmonic components: s mj1 mj2 mj3 mj4 mj5  
            s ≥ 0
            −5 ≤ mji < 5
        """
        logging.debug(n)
        if len(n) != 6:
            raise HarmonicException(f"Doodson array of numbers is wrong length: {len(n)}")
        if n[0]<0 :
            raise HarmonicException(f"Doodson s number is negative: {n[0]}")
        for i in range(1,6): # range(1,6)=1 2 3 4 5
            logging.debug(f"n{i}={n[i]}")
            if n[i] < -5 or n[i] >= 5 :
                raise HarmonicException(f"Doodson value out of bounds: n{i}={n[i]}")
        self.n=n

    def get_speed(self):
        """
        Returns rotation speed in °/h.

        Documentation
        -------------
        | Angle | Period          | Mean longitude  |                 |
        | ----- | --------------- | --------------- | --------------- |
        | tau   | 1.035 days      | Mean lunar time |                 |
        | s     | 27.32 days      | Moon            | 27.321582 days  |
        | h     | 365.24 days     | Sun             | 365.242199 days |
        | p     | 8.85 years      | Lunar perigee   | 8.847 years     |
        | N     | 18.61 years     | Lubar mode      | 18.613 years    |
        | p1    | 209.4 centuries | Solar perigee   | 20940 years     |
        
        tau=15°*t+h-s  
        5 = 277.0248 + 481267.8906*T + 0.0020*T^2 + ...,  
        h = 280.1895 + 36000.7689*T + 0.0003*T^2 + ...,  
        p = 334.3853 + 4069.0340*T — 0.0103*T^2 + ...,  
        N = 100.8432 + 1934.420*T — 0.0021*T^2 + ...,  
        P1 = 281.2209 + 1.7192*T + 0.0005*T^2 + ...,  
        where T is a Julian century of 36,525 mean solar days.  

        Values computed of tau, s, h... are in fact their speed in °/h so doing d/dt.

        - [Lecture 1: Introduction to ocean tides](https://www.whoi.edu/cms/files/lecture01_21351.pdf)
        - [Chapitre 4 Le potentiel générateur des marées](http://fabien.lefevre.free.fr/These_HTML/doc0004.htm)
        """
        return self.n[0]*dtau + self.n[1]*ds + self.n[2]*dh + self.n[3]*dp + self.n[4]*dN + self.n[5]*dp1

def get_by_digits(n0:int,n1:int,n2:int,n3:int,n4:int,n5:int) -> Harmonic:
    """
    Creates an Harmonic object from 6 Doodson digits from 0 to 9.
    """
    return Harmonic([n0,n1-5,n2-5,n3-5,n4-5,n5-5])

def get_by_number(number:int) -> Harmonic:
    """
    Creates a Harmonic object from a Doodson number made of 6 digits. Thus 000000 ≤ number ≤ 999999. 
    """
    n=[None]*6
    n[0]=number//100000
    n[1]=((number%100000)//10000)-5
    n[2]=((number%10000)//1000)-5
    n[3]=((number%1000)//100)-5
    n[4]=((number%100)//10)-5
    n[5]=(number%10)-5
    logging.debug(n)
    return Harmonic(n)
    
# Harmonics constants

# Long period tides
M0=get_by_digits(0,5,5, 5,5,5)
"""M0 Lunar constant (1)(3)."""
S0=get_by_digits(0,5,5, 5,5,5)
"""S0 Solar constant (1)(3)."""
Sa=get_by_digits(0,5,6, 5,5,4)
"""Sa Solar annual (1)(2 difference)."""
Ssa=get_by_digits(0,5,7, 5,5,5)
"""Ssa Solar semiannual (1)(2)(3)."""
Sta=get_by_digits(0,5,8, 5,5,4)
"""Sta (1)."""
Msm=get_by_digits(0,6,3, 6,5,5)
"""Msm (1)."""
Mm=get_by_digits(0,6,5, 4,5,5)
"""Mm Lunar monthly (1)(2)(3)."""
Msf=get_by_digits(0,7,3, 5,5,5)
"""Msf Lunisolar synodic fortnightly (1)(2)."""
Mf=get_by_digits(0,7,5, 5,5,5)
"""Mf Lunisolar fortnightly (1)(2)(3)."""
Mstm=get_by_digits(0,8,3, 6,5,5)
"""Mstm (1)."""
Mtm=get_by_digits(0,8,5, 4,5,5)
"""Mtm (1)."""
Msqm=get_by_digits(0,9,3, 5,5,5)
"""Msqm (1)."""
nodal_M0_1=get_by_digits(0,5,5, 5,6,5)
"""nodal_M0_1 18.613 years, period of lunar node precession (3)."""
nodal_M0_2=get_by_digits(0,7,5, 5,6,5)
"""nodal_M0_2 (3)."""

# Diurnal tides
_2Q1=get_by_digits(1,2,5, 7,5,5)
"""2Q1 Larger elliptic diurnal (1)(2), source difference: speed in (1) 12,8442862 WRONG."""
sigma1=get_by_digits(1,2,7, 5,5,5)
"""sigma1 (1)."""
Q1=get_by_digits(1,3,5, 6,5,5)
"""Q1 Larger lunar elliptic diurnal (1)(2)."""
rau1=get_by_digits(1,3,7, 4,5,5)
"""rau1 Larger lunar evectional diurnal (1)(2), source difference: naming in (2) rau."""
O1=get_by_digits(1,4,5, 5,5,5)
"""O1 Lunar diurnal (1)(2)(3)."""
tau1=get_by_digits(1,4,7, 5,5,5)
"""tau1 (1)."""
# M11   DEPRECTATED (1)
# M12   DEPRECTATED (1)
M1=get_by_digits(1,5,5, 5,5,5)
"""M1 Smaller lunar elliptic diurnal (2)."""
khi1=get_by_digits(1,5,7, 4,5,5)
"""khi1 (1)."""
pi1=get_by_digits(1,6,2, 5,5,6)
"""pi1 (1)."""
P1=get_by_digits(1,6,3, 5,5,5)
"""P1 Solar diurnal (1)(2)(3)."""
# K1L   DUPLICATE (1)
# K1S   DUPLICATE (1)(3)
# K1M   DUPLICATE (3)
K1=get_by_digits(1,6,5, 5,5,5)
"""K1 Lunisolar diurnal  (2)(3)."""
psi1=get_by_digits(1,6,6, 5,5,4)
"""psi1 (1)."""
phi1=get_by_digits(1,6,7, 5,5,5)
"""phi1 (1)."""
teta1=get_by_digits(1,7,3, 6,5,5)
"""teta1 (1)."""
J1=get_by_digits(1,7,5, 4,5,5)
"""J1 Smaller lunar elliptic diurnal (1)(2)."""
# SO1   DATA INCORRECT (1)
OO1=get_by_digits(1,8,5, 5,5,5)
"""OO1 Lunar diurnal (1)(2), source difference: in (1) 185655 wrong."""
nu1=get_by_digits(1,9,5, 4,5,5)
"""nu1 (1)."""
S1=get_by_digits(1,6,4, 5,5,5)
"""S1 Solar diurnal (2)."""
# nodal_O1  DATA INCORRECT (3)
# nodal_K1M DATA INCORRECT (3)

# Semi-diurnal tides
# epsilon2  DATA INCORRECT (1)
_2N2=get_by_digits(2,3,5, 7,5,5)
"""2N2 Lunar elliptical semidiurnal second-order (1)(2), source difference: in (1) 27,9692084 wrong."""
mu2=get_by_digits(2,3,7, 5,5,5)
"""mu2 Variational (1)(2)."""
N2=get_by_digits(2,4,5, 6,5,5)
"""N2 Larger lunar elliptic semidiurnal (1)(2)(3)."""
nu2=get_by_digits(2,4,7, 4,5,5)
"""nu2 Larger lunar evectional (1)(2)."""
M2=get_by_digits(2,5,5, 5,5,5)
"""M2 Principal lunar semidiurnal (1)(2)(3)."""
lambda2=get_by_digits(2,6,3, 6,5,5)
"""lambda2 Smaller lunar evectional (1)(2)."""
L2=get_by_digits(2,6,5, 4,5,5)
"""L2 Smaller lunar elliptic semidiurnal (1)(2), source difference: in (1) 29,5377626 wrong."""
T2=get_by_digits(2,7,2, 5,5,6)
"""T2 Larger solar elliptic (1)(2), source difference: in (1) 29,5589333 wrong."""
S2=get_by_digits(2,7,3, 5,5,5)
"""S2 Principal solar semidiurnal (1)(2)(3)."""
R2=get_by_digits(2,7,4, 5,5,4)
"""R2 Smaller solar elliptic (1)(2 difference)."""
# K2S   DUPLICATE (1)(3)
# K2L   DUPLICATE (1)
# K2M   DUPLICATE (3)
K2=get_by_digits(2,7,5, 5,5,5)
"""K2 Lunisolar semidiurnal (2)(3)."""
_2SM2=get_by_digits(2,9,1, 5,5,5)
"""2SM2 Shallow water semidiurnal (2)."""

# Short period tides
M4=get_by_digits(4,5,5, 5,5,5)
"""M4 Shallow water overtides of principal lunar (2)."""
M6=get_by_digits(6,5,5, 5,5,5)
"""M6 Shallow water overtides of principal lunar (2)."""
MK3=get_by_digits(3,6,5, 5,5,5)
"""MK3 Shallow water terdiurnal (2)."""
S4=get_by_digits(4,9,1, 5,5,5)
"""S4 Shallow water overtides of principal solar (2)."""
MN4=get_by_digits(4,4,5, 6,5,5)
"""MN4 Shallow water quarter diurnal (2)."""
# S6    Shallow water overtides of principal solar DUPLICATE? (2)
M3=get_by_digits(3,5,5, 5,5,5)
"""M3 Lunar terdiurnal (2)."""
_2MK3=get_by_digits(3,4,5, 5,5,5)
"""2MK3 Shallow water terdiurnal (2)."""
M8=get_by_digits(8,5,5, 5,5,5)
"""M8 Shallow water eighth diurnal (2)."""
MS4=get_by_digits(4,7,3, 5,5,5)
"""MS4 Shallow water quarter diurnal (2)."""

# (1): Source [Chapitre 4 Le potentiel générateur des marées](http://fabien.lefevre.free.fr/These_HTML/doc0004.htm)
# (2): Source [Theory of tides - Wikipedia](https://en.wikipedia.org/wiki/Theory_of_tides)
# (3): Source [Lecture 1: Introduction to ocean tides, Myrl Hendershott](https://www.whoi.edu/cms/files/lecture01_21351.pdf)
