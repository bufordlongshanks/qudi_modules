from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors
from hardware.spectrometer.myshamrock import Shamrock


from qtpy import QtCore
import matplotlib.pyplot as plt
from core.module import Base
from core.connector import Connector
from interface.spectrometer_interface import SpectrometerInterface
#from time import strftime, localtime
import time
import numpy as np

class SpectrometerInterface_Andor(Base, SpectrometerInterface):

    fitlogic = Connector(interface='FitLogic')

    def __init__(self, config, **kwargs):
        super().__init__(config=config, **kwargs)
        self.exposure = 0.01
        self.min = 400 #min wavelength
        self.max = 600 #max wavelength
        self.tempset = -50
        self.wavelength = 550
        self.sdk = atmcd('C:\Program Files\Andor SDK')  # Load the atmcd library
        self.spc = Shamrock()  #load the shamrock library
        self.codes = atmcd_codes
        self.length = 1024
        self.num = self.length
        self.imin = 0
        self.imax = self.num
        self.xvals = 0
        self.pixWidth = 1
        self.background = np.zeros(self.num)
        self.corrected = False
        self.use_corrected = False


    def on_activate(self):
        ret = self.sdk.Initialize("")  # Initialize camera
        print("Function Initialize returned {}".format(ret))

        if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:

            (ret, iSerialNumber) = self.sdk.GetCameraSerialNumber()
            print("Function GetCameraSerialNumber returned {} Serial No: {}".format(
                ret, iSerialNumber))

            # Configure the acquisition

            ret = self.sdk.CoolerON()
            print("Function CoolerON returned {}".format(ret))

            ret = self.sdk.SetAcquisitionMode(self.codes.Acquisition_Mode.SINGLE_SCAN)
            print("Function SetAcquisitionMode returned {} mode = Single Scan".format(ret))

            ret = self.sdk.SetReadMode(self.codes.Read_Mode.FULL_VERTICAL_BINNING)
            print("Function SetReadMode returned {} mode = Image".format(ret))

            ret = self.sdk.SetTriggerMode(self.codes.Trigger_Mode.INTERNAL)
            print("Function SetTriggerMode returned {} mode = Internal".format(ret))

            (ret, self.xpixels, ypixels) = self.sdk.GetDetector()
            print("Function GetDetector returned {} xpixels = {} ypixels = {}".format(
                ret, self.xpixels, ypixels))
        else:
            print("Cannot continue, could not initialise camera")


        ret, status = self.sdk.GetStatus()
        if ret == atmcd_errors.Error_Codes.DRV_NOT_INITIALIZED:
            self.log.error('Failed to Connect to Camera, please reload Qudi')
            return
        ret = self.sdk.SetTemperature(self.tempset)
        print("Function SetTemperature returned {} target temperature {}".format(ret, self.tempset))
        ret = self.sdk.CoolerON()
        print("Function CoolerON returned {}".format(ret))

        while ret != atmcd_errors.Error_Codes.DRV_TEMP_STABILIZED:
            time.sleep(5)
            (ret, temperature) = self.sdk.GetTemperature()
            print("Function GetTemperature returned {} current temperature = {} ".format(
                ret, temperature, end=''))
        # Catches above the print statement and preserves the below print statement
        print("")
        print("Temperature stabilized")
        tempinfo = "Function GetTemperature returned {} current temperature = {} ".format(
            ret, temperature)
        self.log.info(tempinfo)

        self.changeExposure(self.exposure)


        (ret, fminExposure, fAccumulate, fKinetic) = self.sdk.GetAcquisitionTimings()
        print("Function GetAcquisitionTimings returned {} exposure = {} accumulate = {} kinetic = {}".format(
            ret, fminExposure, fAccumulate, fKinetic))

        self.length = self.sdk.GetDetector()[1]
        self.pixWidth = self.sdk.GetPixelSize()[1]
        self.spc.SetNumberPixelsSR(0, self.length)
        self.spc.SetPixelWidthSR(0, self.pixWidth)
        self.changeWavelength(self.wavelength)
        print('Grating has {} lines per mm'.format(self.spc.GetGratingInfoSR(0, self.spc.GetGratingSR(0)[1])[1]))
        self.recordBackground()

        self.sdk.PrepareAcquisition()







    def on_deactivate(self):
        return

    def recordBackground(self):
        print(f'TAKING BACKGROUND with exposure time {self.exposure} s')
        print('Block spectrometer in ...')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Taking Background')
        self.sdk.StartAcquisition()
        self.sdk.WaitForAcquisition()
        (ret, arr, validfirst, validlast) = self.sdk.GetImages16(1, 1, self.length)
        print('DONE')
        self.corrected = True
        self.background = arr
        return

    def recordSpectrum(self):

        data = np.empty((2, self.num), dtype=np.double)
        data[0] = self.xvals


        self.sdk.StartAcquisition()
        self.sdk.WaitForAcquisition()
        (ret, arr, validfirst, validlast) = self.sdk.GetImages16(1, 1, self.length)
        if self.corrected == True and self.use_corrected == True:
            data[1] = arr[self.imin:self.imax + 1] - self.background[self.imin:self.imax + 1]
        else:
            data[1] = arr[self.imin:self.imax+1]

        self.sdk.CoolerON()

        return data

    def setExposure(self, exposureTime):

        ret = self.sdk.SetExposureTime(exposureTime)
        print("Function SetExposureTime returned {} time = 0.01s".format(ret))

        (ret, fminExposure, fAccumulate, fKinetic) = self.sdk.GetAcquisitionTimings()
        print("Function GetAcquisitionTimings returned {} exposure = {} accumulate = {} kinetic = {}".format(
            ret, fminExposure, fAccumulate, fKinetic))

        ret = self.sdk.PrepareAcquisition()
        print("Function PrepareAcquisition returned {}".format(ret))
        self.exposure = exposureTime
        self.corrected = False
        if self.use_corrected == True:
            print('Take new background')
        return

    def getExposure(self):
        return self.exposure

    def changeWavelength(self, wavelength):
        self.spc.SetWavelengthSR(0, wavelength)
        self.wavelength = wavelength
        xdata = np.array(self.spc.GetCalibrationSR(0, self.length)[1])
        self.imin = (np.abs(xdata - self.min)).argmin()
        print('Minimum set to {} nm'.format(xdata[self.imin]))
        self.imax = (np.abs(xdata - self.max)).argmin()
        print('Maximum set to {} nm'.format(xdata[self.imax]))
        self.xvals = xdata[self.imin:self.imax+1]
        self.num = self.xvals.size
        print('Wavelength set to {} nm'.format(self.wavelength))
        self.corrected = False
        if self.use_corrected == True:
            print('Take new background')
        return

    def changeRangeMin(self, min):
        self.min = min
        xdata = np.array(self.spc.GetCalibrationSR(0, self.length)[1])
        self.imin = (np.abs(xdata - self.min)).argmin()
        print('Minimum set to {} nm'.format(xdata[self.imin]))
        self.xvals = xdata[self.imin:self.imax + 1]
        self.num = self.xvals.size
        return

    def changeRangeMax(self, max):
        self.max = max
        xdata = np.array(self.spc.GetCalibrationSR(0, self.length)[1])
        self.imax = (np.abs(xdata - self.max)).argmin()
        print('Maximum set to {} nm'.format(xdata[self.imax]))
        self.xvals = xdata[self.imin:self.imax + 1]
        self.num = self.xvals.size
        return

    def switchMode(self, state):
        if state == QtCore.Qt.Checked:
            self.use_corrected = True
            if self.corrected == False:
                print('No valid background may be used - Take new background')
            else:
                print('Using background correction')
        else:
            self.use_corrected = False
        return

    def changeGrating(self, gra):
        self.spc.SetGratingSR(0, gra)
        print('Grating has {} lines per mm'.format(self.spc.GetGratingInfoSR(0, self.spc.GetGratingSR(0)[1])[1]))
        self.changeWavelength(self.wavelength)
        self.corrected = False
        if self.use_corrected == True:
            print('Take new background')
        return

    def changeExposure(self, exposure):
        ret = self.sdk.SetExposureTime(exposure)
        self.exposure = exposure
        print("Function SetExposureTime returned {} time = {}".format(ret, self.exposure))
        self.corrected = False
        if self.use_corrected == True:
            print('Take new background')
        return

    def on_deactivate(self):
        ret = self.sdk.ShutDown()
        print("Function Shutdown returned {}".format(ret))
        return




