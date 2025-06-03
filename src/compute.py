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