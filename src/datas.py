# coding: utf-8
"""
This module contains stuff for data handling.
"""

import conf_logging
import logging
from datetime import datetime
from pathlib import Path
import re
import datetime

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

    def __eq__(self,other):
        if isinstance(other,Data):
            return self.t==other.t and self.height==other.height
        return NotImplemented





from zoneinfo import ZoneInfo
RE_COMMENT_PATTERN=re.compile(r'\s*#.*')
RE_DATA_PATTERN=re.compile(r'\s*([0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2});([0-9\.]+);3\s*')
def reader(files:list[Path],tzinfo="UTC"):
    data_list=[]
    for file in files:
        logger.debug(file)
        with open(file, 'r') as f:
            logger.info(f"Read {file}")
            for line in f:
                line=line.strip()
                m=RE_DATA_PATTERN.fullmatch(line)
                if m:
                    t=datetime.datetime.strptime(m.group(1),"%d/%m/%Y %H:%M:%S")
                    t=t.replace(tzinfo=ZoneInfo(tzinfo))
                    height=float(m.group(2))
                    logger.debug(f"DATA: {t.strftime("%d/%m/%Y %H:%M:%S [%z]")}: {height}")
                    data_list.append(Data(t,height))
                else:
                    m=RE_COMMENT_PATTERN.fullmatch(line)
                    if m:
                        logger.debug(f"COMMENT: {line}")
                    else:
                        logger.warn(f"ERROR: '{line}'")    
    return data_list