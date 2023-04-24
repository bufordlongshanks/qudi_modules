

from core.module import Base
from interface.slow_counter_interface import SlowCounterInterface
from interface.spectrometer_interface import SpectrometerInterface
from time import sleep
import TimeTagger

class timetagger_interface(Base, SpectrometerInterface):

    def __init__(self, config, **kwargs):
        super().__init__(config=config, **kwargs)
        self.exposure = 0.1

    def on_activate(self):
        self.tagger = TimeTagger.createTimeTagger()
        self.countrate = TimeTagger.Countrate(tagger=self.tagger, channels=[-1])
        self.tagger.setTriggerLevel(-1, -0.6)
        self.countrate.stop()

    def recordData(self):
        self.countrate.start()
        self.countrate.clear()
        self.countrate.startFor(self.exposure*1e12)
        self.countrate.waitUntilFinished()
        data = self.countrate.getCountsTotal()[0]

        self.countrate.stop()

        return data

    def recordSpectrum(self):
        return

    def setExposure(self, exposureTime):
        self.exposure = exposureTime
        print('exposure time set to {} s'.format(exposureTime))
        return

    def getExposure(self):
        return self.exposure