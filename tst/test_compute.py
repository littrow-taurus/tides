import conf_logging
import logging
import unittest
from models import Model_N3
from models import Model_N6
from models import Model_N10
from models import Model_N16
from models import Model_N24
from models import Model_N32
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from datas import Data
import compute
import datas
from pathlib import Path
import random
from models import ModelError
import matplotlib.pyplot as plt

logger=logging.getLogger(__name__)

ROOT_DIR=Path(__file__).parents[1]
REFMAR_DIR=ROOT_DIR / "data" / "REFMAR"

class TestCompute(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        files=[f for f in REFMAR_DIR.glob("111_*.txt")]
        self.data_list=datas.reader(files)


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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
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
        model.amplitudes_cos[2]=0.5 # S2=0.5
        model.amplitudes_sin[2]=0.5 # S2=0.5
        model.amplitudes_cos[3]=0.1 # N2=0.1
        model.amplitudes_sin[3]=1.1 # N2=1.1
        # Build a fake set of data from 2000-01-01 to 2010-01-01 Te=15mn
        t=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2003,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_test=[]
        while t < t_end:
            height=model.get_height(t)
            data_test.append(Data(t,height))
            t+=timedelta(minutes=15)
        model_test=Model_N3()
        err=compute.fourier_transform(model_test,data_test)
        logger.info(err)
        for i in range(len(model_test.harmonics)):
            logger.debug(f"speed[{i}]: {model.harmonics[i].get_speed():.2f}°/h")
            logger.debug(f"cos[{i}]: {model_test.amplitudes_cos[i]:.4f}")
            logger.debug(f"sin[{i}]: {model_test.amplitudes_sin[i]:.4f}")
        for i in range(len(model_test.harmonics)):
            self.assertAlmostEqual(model_test.amplitudes_cos[i],model.amplitudes_cos[i],delta=0.01)
            self.assertAlmostEqual(model_test.amplitudes_sin[i],model.amplitudes_sin[i],delta=0.01)

    def test_fourier_transform_N3_spot111(self):
        model=Model_N3()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(err)
        self.assertLess(err.abs,1.0)
        t0=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        for i in range(10):
            r_d=random.randrange(0,365*20)
            r_h=random.randrange(0,24)
            r_m=random.randrange(0,60,10)
            t=t0+timedelta(days=r_d,hours=r_h,minutes=r_m)
            height_est=model.get_height(t)
            for d in self.data_list:
                if d.t==t:                    
                    height_ref=d.height
                    logger.info(f"{t}: {height_est:0.3f} / {height_ref:0.3f} (delta={height_est-height_ref:0.3f})")
#                    self.assertLess(height_est-height_ref,1.0)

    def test_fourier_transform_N10_spot111(self):
        model=Model_N10()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(err)
        self.assertLess(err.abs,1.0)
        t0=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        for i in range(10):
            r_d=random.randrange(0,365*20)
            r_h=random.randrange(0,24)
            r_m=random.randrange(0,60,10)
            t=t0+timedelta(days=r_d,hours=r_h,minutes=r_m)
            height_est=model.get_height(t)
            for d in self.data_list:
                if d.t==t:                    
                    height_ref=d.height
                    logger.info(f"{t}: {height_est:0.3f} / {height_ref:0.3f} (delta={height_est-height_ref:0.3f})")
#                    self.assertLess(height_est-height_ref,1.0)
                    
        t_start=datetime(2025,3,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2025,3,5,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_ref=[d for d in self.data_list if d.t>=t_start and d.t<t_end]
        data_mod=[]
        delta_list=[]
        for d in data_ref:
            d_mod=Data(d.t,model.get_height(d.t))
            data_mod.append(d_mod)
            delta_list.append(d_mod.height-d.height)
        height_ref=[d.height for d in data_ref]
        height_mod=[d.height for d in data_mod]
        t_ref=[d.t for d in data_ref]
        t_mod=[d.t for d in data_mod]
        plt.plot(t_ref,height_ref)
        plt.plot(t_mod,height_mod)
        plt.plot(t_mod,delta_list)
        plt.show()

    def test_fourier_transform_N16_spot111(self):
        model=Model_N16()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(err)
        self.assertLess(err.abs,1.0)
        t0=datetime(2000,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        for i in range(10):
            r_d=random.randrange(0,365*20)
            r_h=random.randrange(0,24)
            r_m=random.randrange(0,60,10)
            t=t0+timedelta(days=r_d,hours=r_h,minutes=r_m)
            height_est=model.get_height(t)
            for d in self.data_list:
                if d.t==t:                    
                    height_ref=d.height
                    logger.info(f"{t}: {height_est:0.3f} / {height_ref:0.3f} (delta={height_est-height_ref:0.3f})")
#                    self.assertLess(height_est-height_ref,1.0)
                    
        t_start=datetime(2025,3,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2025,3,5,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_ref=[d for d in self.data_list if d.t>=t_start and d.t<t_end]
        data_mod=[]
        delta_list=[]
        for d in data_ref:
            d_mod=Data(d.t,model.get_height(d.t))
            data_mod.append(d_mod)
            delta_list.append(d_mod.height-d.height)
        height_ref=[d.height for d in data_ref]
        height_mod=[d.height for d in data_mod]
        t_ref=[d.t for d in data_ref]
        t_mod=[d.t for d in data_mod]
        plt.plot(t_ref,height_ref)
        plt.plot(t_mod,height_mod)
        plt.plot(t_mod,delta_list)
        plt.show()

    def test_fourier_transform_all_models_perfs_spot111(self):
        model=Model_N3()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N3:\n{err}")
    

        model=Model_N6()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N6:\n{err}")
    

        model=Model_N10()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N10:\n{err}")
        
        model=Model_N16()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N16:\n{err}")
    

        model=Model_N24()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N24:\n{err}")
    

        model=Model_N32()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N32:\n{err}")
    
    def test_now_spot111(self):
        model=Model_N16()
        err=compute.fourier_transform(model,self.data_list)
        logger.info(f"Model_N16:\n{err}")
        now=datetime.now(timezone.utc)
        t=now.replace(hour=0,minute=0,second=0,microsecond=0)
        t_end=now.replace(hour=23,minute=59,second=59,microsecond=0)
        while t<=t_end:
            logger.info(f"{t}: {model.get_height(t)}")
            t+=timedelta(minutes=10)
        logger.info(f"Now: {model.get_height(now):0.3f}")

    def test_tune_harmonic(self):
        t_start=datetime(2024,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2025,1,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_ref=[d for d in self.data_list if d.t>=t_start and d.t<t_end]

        model=Model_N3()
        err=compute.fourier_transform(model,data_ref)
        logger.info(f"Before tuning:\n{err}")

        model_tuned=compute.tune_harmonic(model,0,0.1,4,data_ref)
        model_tuned=compute.tune_harmonic(model,1,0.1,4,data_ref)
        model_tuned=compute.tune_harmonic(model,2,0.1,4,data_ref)
        model_tuned=compute.tune_harmonic(model,3,0.1,4,data_ref)
        err_tuned=ModelError(model_tuned,data_ref)
        logger.info(f"After tuning:\n{err_tuned}")

        t_start=datetime(2025,3,1,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        t_end=datetime(2025,3,5,hour=0,minute=0,second=0,tzinfo=timezone.utc)
        data_ref=[d for d in self.data_list if d.t>=t_start and d.t<t_end]
        data_mod=[]
        data_mod_tuned=[]
        for d in data_ref:
            d_mod=Data(d.t,model.get_height(d.t))
            data_mod.append(d_mod)
            d_mod_tuned=Data(d.t,model_tuned.get_height(d.t))
            data_mod_tuned.append(d_mod_tuned)
        height_ref=[d.height for d in data_ref]
        height_mod=[d.height for d in data_mod]
        height_mod_tuned=[d.height for d in data_mod_tuned]
        t_ref=[d.t for d in data_ref]
        plt.plot(t_ref,height_ref)
        plt.plot(t_ref,height_mod)
        plt.plot(t_ref,height_mod_tuned)
        plt.show()
