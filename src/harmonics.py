import logging
import datetime

logger=logging.getLogger(__name__)

APPLY_TIME_CORRECTION=True
# See below
# tau=15°*t+h-s  
# s = 277.0248 + 481267.8906*T + 0.0020*T^2 + ...,  
# h = 280.1895 + 36000.7689*T + 0.0003*T^2 + ...,  
# p = 334.3853 + 4069.0340*T — 0.0103*T^2 + ...,  
# N = 100.8432 + 1934.420*T — 0.0021*T^2 + ...,  
# P1 = 281.2209 + 1.7192*T + 0.0005*T^2 + ...,  
# where T is a Julian century of 36,525 mean solar days (start 1899-12-31=T0). So T=t/36525*24 if t is hours.
#
# s = 277.0248 + 481267.8906*(t/36525*24) + 0.0020*(t/36525*24)^2 + ..., where t is time in hours from T0.  
# ds/dt = 481267.8906/(36525*24) + 0.0020*2*(t/36525*24)
# ds/dt = (481267.8906+2*0.0020*t)/36525*24
#
# tau=15°*t+h-s
# dtau/dt=15+dh/dt-ds/dt
#
# In the program ds/dt is called ds.
T0=datetime.datetime(1900,1,1,hour=0,minute=0,second=0)
_t=0
if APPLY_TIME_CORRECTION:
    _t=(datetime.datetime.now()-T0).days/36525
ds=(481267.8906+2*0.0020*_t)/36525/24
dh=(36000.7689+2*0.0003*_t)/36525/24
dp=(4069.0340+2*0.0103*_t)/36525/24
dN=(1934.420+2*0.0021*_t)/36525/24
dp1=(1.71920+2*0.0005*_t)/36525/24
dtau=15+dh-ds

class DoodsonException(Exception):
    pass

class Doodson:
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

    def __init__(self,n:list):
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
            raise DoodsonException(f"Doodson array of numbers is wrong length: {len(n)}")
        if n[0]<0 :
            raise DoodsonException(f"Doodson s number is negative: {n[0]}")
        for i in range(1,6): # range(1,6)=1 2 3 4 5
            logging.debug(f"n{i}={n[i]}")
            if n[i] < -5 or n[i] >= 5 :
                raise DoodsonException(f"Doodson value out of bounds: n{i}={n[i]}")
        self.n=n

    def get_frequency(self):
        """
        Returns frequency in °/h.


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

def get_by_digits(n0:int,n1:int,n2:int,n3:int,n4:int,n5:int) -> Doodson:
    """
    Creates a Doodson object from 6 digits from 0 to 9.
    """
    return Doodson([n0,n1-5,n2-5,n3-5,n4-5,n5-5])

def get_by_number(number:int) -> Doodson:
    """
    Creates a Doodson object from a Doodson number made of 6 digits. Thus 000000 ≤ number ≤ 999999. 
    """
    n=[None]*6
    n[0]=number//100000
    n[1]=((number%100000)//10000)-5
    n[2]=((number%10000)//1000)-5
    n[3]=((number%1000)//100)-5
    n[4]=((number%100)//10)-5
    n[5]=(number%10)-5
    logging.debug(n)
    return Doodson(n)
    