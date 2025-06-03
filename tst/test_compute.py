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
    def test_fourier_transform_N3_c100(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=1.0 # M2
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=0.0 # S2
        model.amplitudes_sin[2]=0.0 # S2
        model.amplitudes_cos[3]=0.0 # N2
        model.amplitudes_sin[3]=0.0 # N2
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2010,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_c010(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.0 # M2
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=1.0 # S2
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
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_c001(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.0 # M2
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=0.0 # S2
        model.amplitudes_sin[2]=0.0 # S2
        model.amplitudes_cos[3]=1.0 # N2
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
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_s100(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.0 # M2
        model.amplitudes_sin[1]=1.0 # M2
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
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_s010(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.0 # M2
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=0.0 # S2
        model.amplitudes_sin[2]=1.0 # S2
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
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_s001(self):
        model=Model_N3()
        model.amplitudes_cos[0]=0.0 # M0
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.0 # M2
        model.amplitudes_sin[1]=0.0 # M2
        model.amplitudes_cos[2]=0.0 # S2
        model.amplitudes_sin[2]=0.0 # S2
        model.amplitudes_cos[3]=0.0 # N2
        model.amplitudes_sin[3]=1.0 # N2
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2010,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_000(self):
        model=Model_N3()
        model.amplitudes_cos[0]=1.0 # M0
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
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_myxz(self):
        model=Model_N3()
        model.amplitudes_cos[0]=2.5 # M0=2.5
        model.amplitudes_sin[0]=0.0 # M0
        model.amplitudes_cos[1]=0.8 # M2=0.8
        model.amplitudes_sin[1]=0.4 # M2=0.4
        model.amplitudes_cos[2]=0.0 # S2=0.5
        model.amplitudes_sin[2]=0.0 # S2=0.5
        model.amplitudes_cos[3]=0.0 # N2=0.1
        model.amplitudes_sin[3]=0.0 # N2=1.1
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2020,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        model_test=Model_N3()
        compute.fourier_transform(model_test,data_test)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)
