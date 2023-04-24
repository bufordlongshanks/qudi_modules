from ctypes import *
import ctypes.util
import os
ERROR_CODE = {

        20201: "SHAMROCK_COMMUNICATION_ERROR",
        20202: "SHAMROCK_SUCCESS",
        20266: "SHAMROCK_P1INVALID",
        20267: "SHAMROCK_P2INVALID",
        20268: "SHAMROCK_P3INVALID",
        20269: "SHAMROCK_P4INVALID",
        20270: "SHAMROCK_P5INVALID",
        20275: "SHAMROCK_NOT_INITIALIZED",
        20292: "SHAMROCK_NOT_AVAILABLE"
    }
class Shamrock:

    def __init__(self, userpath = 'C:\Program Files\Andor SDK\Shamrock64'):
        self.dll = self._load_library(userpath)

        print("Initializing Shamrock...", )
        error = self.dll.ShamrockInitialize()

        nodevices = c_int()
        error = self.dll.ShamrockGetNumberDevices(byref(nodevices))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        print(f'(Nr of devices: {nodevices.value})')

        # Initiate parameters - Shamrock
        self.NrPixels = 0

    def _load_library(self, userpath):
        _path = userpath + ';' + os.environ['PATH']
        os.environ['PATH'] = _path
        dllname = "ShamrockCIF.dll"
        path = ctypes.util.find_library(dllname)
        return windll.LoadLibrary(path)

    def __del__(self):
        error = self.dll.ShamrockClose()
        if error != 20202:
            raise IOError(ERROR_CODE[error])

    def close(self):
        error = self.dll.ShamrockClose()
        if error != 20202:
            raise IOError(ERROR_CODE[error])

    def GetNumberDevicesSR(self):
        nodevices = c_int()
        error = self.dll.ShamrockGetNumberDevices(byref(nodevices))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], nodevices.value

    def GetFunctionReturnDescriptionSR(self, error, MaxDescStrLen):
        error = c_int(error)
        MaxDescStrLen = c_int(MaxDescStrLen)
        description = c_char_p()
        error = self.dll.ShamrockGetFunctionReturnDescription(error, description, MaxDescStrLen)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], description.value

    # ---- sdkeeprom functions

    def GetSerialNumberSR(self, device):
        device = c_int(device)
        serial = ctypes.create_string_buffer(128)
        error = self.dll.ShamrockGetSerialNumber(device, byref(serial))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], serial.value

    def EepromGetOpticalParamsSR(self, device):
        device = c_int(device)
        FocalLength = c_float()
        AngularDeviation = c_float()
        FocalTilt = c_float()
        error = self.dll.ShamrockEepromGetOpticalParams(device, byref(FocalLength),
                                                    byref(AngularDeviation), byref(FocalTilt))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], FocalLength.value, AngularDeviation.value, FocalTilt.value

    # ---- sdkgrating functions
    def SetGratingSR(self, device, grating):
        device = c_int(device)
        grating = c_int(grating)
        error = self.dll.ShamrockSetGrating(device, grating)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error]

    def GetGratingSR(self, device):
        device = c_int(device)
        grating = c_int()
        error = self.dll.ShamrockGetGrating(device, byref(grating))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], grating.value

    def WavelengthResetSR(self, device):
        device = c_int(device)
        error = self.dll.ShamrockWavelengthReset(device)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error]

    def GetNumberGratingsSR(self, device):
        device = c_int(device)
        noGratings = c_int()
        error = self.dll.ShamrockGetNumberGratings(device, byref(noGratings))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], noGratings.value

    def GetGratingInfoSR(self, device, grating):
        device = c_int(device)
        grating = c_int(grating)
        Lines = c_float()
        Blaze = ctypes.create_string_buffer(128)
        Home = c_int()
        Offset = c_int()
        error = self.dll.ShamrockGetGratingInfo(device, grating,
                                            byref(Lines), byref(Blaze), byref(Home), byref(Offset))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], Lines.value, Blaze.value.decode(), Home.value, Offset.value

    # ---- sdkwavelength functions
    def SetWavelengthSR(self, device, wavelength):
        device = c_int(device)
        wavelength = c_float(wavelength)
        error = self.dll.ShamrockSetWavelength(device, wavelength)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error]

    def GetWavelengthSR(self, device):
        device = c_int(device)
        wavelength = c_float()
        error = self.dll.ShamrockGetWavelength(device, byref(wavelength))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], wavelength.value

    def GetWavelengthLimitsSR(self, device, grating):
        device = c_int(device)
        grating = c_int(grating)
        minLambda = c_float()
        maxLambda = c_float()
        error = self.dll.ShamrockGetWavelengthLimits(device, grating, byref(minLambda), byref(maxLambda))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], minLambda.value, maxLambda.value

    def GotoZeroOrderSR(self, device):
        device = c_int(device)
        error = self.dll.ShamrockGotoZeroOrder(device)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error]

    def AtZeroOrderSR(self, device):
        device = c_int(device)
        atZeroOrder = c_int()
        error = self.dll.ShamrockAtZeroOrder(device, byref(atZeroOrder))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], atZeroOrder.value

    # ---- sdkcalibration functions
    def SetNumberPixelsSR(self, device, NumberPixels):
        device = c_int(device)
        NumberPixels = c_int(NumberPixels)
        error = self.dll.ShamrockSetNumberPixels(device, NumberPixels)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        self.NrPixels = NumberPixels.value
        return ERROR_CODE[error]

    def SetPixelWidthSR(self, device, Width):
        device = c_int(device)
        Width = c_float(Width)
        error = self.dll.ShamrockSetPixelWidth(device, Width)
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error]

    def GetNumberPixelsSR(self, device):
        device = c_int(device)
        NumberPixels = c_int()
        error = self.dll.ShamrockGetNumberPixels(device, byref(NumberPixels))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        self.NrPixels = NumberPixels.value
        return ERROR_CODE[error], NumberPixels.value

    def GetPixelWidthSR(self, device):
        device = c_int(device)
        Width = c_float()
        error = self.dll.ShamrockGetPixelWidth(device, byref(Width))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], Width.value



    def GetCalibrationSR(self, device, Npxls):
        device = c_int(device)
        CalibrationValues = (c_float * int(Npxls))()
        error = self.dll.ShamrockGetCalibration(device, byref(CalibrationValues), int(Npxls))
        if error != 20202:
            raise IOError(ERROR_CODE[error])
        return ERROR_CODE[error], CalibrationValues[:]

    # ####################################################

    # List of error codes

