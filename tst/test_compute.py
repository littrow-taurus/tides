import conf_logging
import logging
import unittest
from models import Model_N3
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from datas import Data
import compute

logger=logging.getLogger(__name__)

class TestCompute(unittest.TestCase):
    def test_fourier_transform_N3_100(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=1.0 # M2=1
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=0.0 # S2
        model.amplitudes_sin[2]=0.0 # S2
        model.amplitudes_cos[3]=0.0 # N2
        model.amplitudes_sin[3]=0.0 # N2
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2010,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        model_test=Model_N3()
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_000(self):
        model=Model_N3()
        model.amplitudes_cos[0]=1.0 # M0=1
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.0 # M2
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=0.0 # S2
        model.amplitudes_sin[2]=0.0 # S2
        model.amplitudes_cos[3]=0.0 # N2
        model.amplitudes_sin[3]=0.0 # N2
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2010,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        model_test=Model_N3()
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_111(self):
        model=Model_N3()
        model.amplitudes_cos[0]=2.5 # M0=2.5
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.8 # M2=0.8
        model.amplitudes_sin[1]=0.4 # M2=0.4
        model.amplitudes_cos[2]=0.5 # S2=0.5
        model.amplitudes_sin[2]=0.5 # S2=0.5
        model.amplitudes_cos[3]=0.1 # N2=0.1
        model.amplitudes_sin[3]=1.1 # N2=1.1
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2010,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        model_test=Model_N3()
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(model_test.amplitudes_cos[i])
            logger.debug(model_test.amplitudes_sin[i])
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)
