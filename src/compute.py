# coding: utf-8
"""
This module contains functions that computes a model based on estimations.
"""

import conf_logging
import logging
import models
from models import Model
from datas import Data
import math
from models import ModelError
import copy 

logger=logging.getLogger(__name__)

def fourier_transform(model:Model,data_list:list[Data]) -> ModelError:
    """
    Uses Fourier transformation to compute amplitudes of model. If any data was already present they are overriden.
    
    Ac(i) = [ Ʃ data(dh) * cos(w(i)*dh) ] / N
    As(i) = [ Ʃ data(dh) * sin(w(i)*dh) ] / N
    where w: rotation speed (°/h)
    and N: number of data

    :param model: Model to compute (full reset of model's data)
    :type model: Model
    :param data_list: List of data used to compute the model
    :type model: list[Data]
    :return: Error measurement of model
    :rtype: ModelError
    :return: The model error computed with the list of data provided
    :rtype: ModelError
    """
    N=len(data_list)
    for i in range(len(model.harmonics)):
        model.amplitudes_cos[i]=0
        model.amplitudes_sin[i]=0
    for data in data_list:
        dh=models.get_hour(data.t) # time from T0 in hours 
        for i in range(len(model.harmonics)):
            angle=math.radians(model.harmonics[i].get_speed()*dh)
            model.amplitudes_cos[i]+=data.height*math.cos(angle)
            model.amplitudes_sin[i]+=data.height*math.sin(angle)
    for i in range(len(model.harmonics)):
        if model.harmonics[i].get_speed()!=0.0:
            model.amplitudes_cos[i]=model.amplitudes_cos[i]*2/N
            model.amplitudes_sin[i]=model.amplitudes_sin[i]*2/N
        else:
            model.amplitudes_cos[i]=model.amplitudes_cos[i]/N
            model.amplitudes_sin[i]=model.amplitudes_sin[i]/N
    return ModelError(model,data_list)

def tune_harmonic_grid(model:Model,harmonic_index:int,R:float,N:int,data_list:list[Data]) -> Model:
    """
    Fine tunes a single harmonic using grid method in a model using a data list. This tuning is made adjusting slightly both amplitudes (cos and sin) to reduce error.  

    Lets consider the harmonic is a 2D vector whose coordinates are both amplitudes. We note those coordinates c and s. We move c and s from their original values c0 and s0 as follow:
    c = c0 + n*d
    s = s0 + m*d
    with d = R/N * sqrt(c0^2 + s0^2)
    and n, m in [-N, -N+1, ..., N-1, N]

    :param model: Model to be tuned
    :type model: Model
    :param harmonic_index: Index of sole harmonic in the model that is to be modified
    :type harmonic: int
    :param R: Fraction of module amplitude that will be used as max step for modification of amplitudes
    :type R: float
    :param N: Number of steps explored
    :type N: int
    :param data_list: Data list to measure error and evaluate the best tuning
    :type data_list: list[Data]
    :return: The best model obtained according to above exploration 
    :rtype: Model
    :return: Error of tuned model
    :rtype: ModelError
    """
    c0=model.amplitudes_cos[harmonic_index]
    s0=model.amplitudes_sin[harmonic_index]
    d=R/N*math.sqrt(c0**2+s0**2)
    model_best=copy.copy(model)
    err_best=ModelError(model_best,data_list)

    for c_step in range(-N,N+1):
        c=c0+c_step*d
        for s_step in range(-N,N+1):
            s=s0+s_step*d
            model_tune=copy.copy(model)
            model_tune.amplitudes_cos[harmonic_index]=c
            model_tune.amplitudes_sin[harmonic_index]=s
            err_tune=ModelError(model_tune,data_list)
            if max(err_tune.max,math.fabs(err_tune.min))<max(err_best.max,math.fabs(err_best.min)):
#            if err_tune.max<=err_best.max and err_tune.min>=err_best.min:
#            if err_tune.var<err_best.var:
#            if err_tune.abs<err_best.abs:
                model_best=model_tune
                err_best=err_tune    
    return model_best,err_best

def tune_harmonic_amp(model:Model,harmonic_index:int,R:float,N:int,data_list:list[Data]) -> Model:
    """
    Fine tunes a single harmonic using amplitude method in a model using a data list. This tuning is made adjusting slightly both amplitudes (cos and sin) to reduce error.  

    Lets consider the harmonic is a 2D vector whose coordinates are both amplitudes. We note those coordinates c and s. We move c and s from their original values c0 and s0 as follow:
    c = c0 * (1 + n*d)
    s = s0 * (1 + n*d)
    with d = R/N
    and n in [-N, -N+1, ..., N-1, N]

    :param model: Model to be tuned
    :type model: Model
    :param harmonic_index: Index of sole harmonic in the model that is to be modified
    :type harmonic: int
    :param R: Fraction of module amplitude that will be used as max step for modification of amplitudes
    :type R: float
    :param N: Number of steps explored
    :type N: int
    :param data_list: Data list to measure error and evaluate the best tuning
    :type data_list: list[Data]
    :return: The best model obtained according to above exploration 
    :rtype: Model
    :return: Error of tuned model
    :rtype: ModelError
    """
    c0=model.amplitudes_cos[harmonic_index]
    s0=model.amplitudes_sin[harmonic_index]
    model_best=Model(model.harmonics.copy())
    model_best.amplitudes_cos=model.amplitudes_cos.copy()
    model_best.amplitudes_sin=model.amplitudes_sin.copy()
    err_best=ModelError(model_best,data_list)

    for n in range(-N,N+1):
        # -N ≤ n ≤ N
        # -R ≤ n*R/N ≤ R
        # c0(1-R) ≤ c ≤ c0(1+R)
        c=c0*(1+n*R/N)
        # s0(1-R) ≤ s ≤ s0(1+R)
        s=s0*(1+n*R/N)
        model_tune=Model(model.harmonics.copy())
        model_tune.amplitudes_cos=model.amplitudes_cos.copy()
        model_tune.amplitudes_sin=model.amplitudes_sin.copy()
        model_tune.amplitudes_cos[harmonic_index]=c
        model_tune.amplitudes_sin[harmonic_index]=s
        err_tune=ModelError(model_tune,data_list)
        if max(err_tune.max,math.fabs(err_tune.min))<max(err_best.max,math.fabs(err_best.min)):
#        if err_tune.max<=err_best.max and err_tune.min>=err_best.min:
#        if err_tune.var<err_best.var:
#        if err_tune.abs<err_best.abs:
            model_best=model_tune
            err_best=err_tune
    
    return model_best,err_best

def tune_harmonic_ang(model:Model,harmonic_index:int,R:float,N:int,data_list:list[Data]) -> Model:
    """
    Fine tunes a single harmonic using aangular method in a model using a data list. This tuning is made adjusting slightly angular composition of cos and sin to reduce error.  

    Lets consider the harmonic is a 2D vector whose coordinates are both amplitudes. We note those coordinates c and s. We move c and s from their original values c0 and s0 as follow:
    a0=atan2(c0,s0)
    M=sqrt(c0^2 + s0^2)
    a = a0 + PI*d*n
    c = M * cos(a) 
    s = M * sin(a)
    with d = R/N
    and n in [-N, -N+1, ..., N-1, N]

    :param model: Model to be tuned
    :type model: Model
    :param harmonic_index: Index of sole harmonic in the model that is to be modified
    :type harmonic: int
    :param R: Fraction of PI rad (or 180°) that will be used as max step for modification of amplitudes
    :type R: float
    :param N: Number of steps explored
    :type N: int
    :param data_list: Data list to measure error and evaluate the best tuning
    :type data_list: list[Data]
    :return: The best model obtained according to above exploration 
    :rtype: Model
    :return: Error of tuned model
    :rtype: ModelError
    """
    c0=model.amplitudes_cos[harmonic_index]
    s0=model.amplitudes_sin[harmonic_index]
    a0=math.atan2(c0,s0)
    M=math.sqrt(c0**2 + s0**2)
    model_best=Model(model.harmonics.copy())
    model_best.amplitudes_cos=model.amplitudes_cos.copy()
    model_best.amplitudes_sin=model.amplitudes_sin.copy()
    err_best=ModelError(model_best,data_list)

    for n in range(-N,N+1):
        # -N ≤ n ≤ N
        # -R ≤ n*R/N ≤ R
        # -R*PI ≤ PI*(1+n*R/N) ≤ R*PI
        # a0-R*PI ≤ a0 + PI*(1+n*R/N) ≤ a0+R*PI
        a=a0+math.pi*(1+n*R/N)
        c=M*math.cos(a)
        s=M*math.sin(a)
        model_tune=Model(model.harmonics.copy())
        model_tune.amplitudes_cos=model.amplitudes_cos.copy()
        model_tune.amplitudes_sin=model.amplitudes_sin.copy()
        model_tune.amplitudes_cos[harmonic_index]=c
        model_tune.amplitudes_sin[harmonic_index]=s
        err_tune=ModelError(model_tune,data_list)
        if max(err_tune.max,math.fabs(err_tune.min))<max(err_best.max,math.fabs(err_best.min)):
#        if err_tune.max<=err_best.max and err_tune.min>=err_best.min:
#        if err_tune.var<err_best.var:
#        if err_tune.abs<err_best.abs:
            model_best=model_tune
            err_best=err_tune
    
    return model_best,err_best
