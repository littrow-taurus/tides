# coding: utf-8
"""
This module contains stuff for data handling.
"""

import conf_logging
import logging
from datetime import datetime

logger=logging.getLogger(__name__)

class Data:
    """
    This class holds a single data, i.e date time and tide's height at that moment.

    :param t: Date time for data.
    :type t: datetime MUST be aware (oposite to naive).
    :param height: Tide's height (m).
    :type height: float
    """

    def __init__(self,t:datetime,height:float):
        """
        Constructor.

        :param t: Date time for data.
        :type datetime: MUST be aware (oposite to naive).
        :param height: Tide's height (m).
        :type height: float
        """
        if t.tzinfo is None:
            raise ValueError("Data is not datetime aware")
        self.t=t
        self.height=height
