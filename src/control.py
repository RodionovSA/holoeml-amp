import numpy as np

from pylablib.devices import Thorlabs
from pythorcam.camera_cs126 import Camera_CS126
from src.monochromator.mono_class import MonochromatorControl

class Control:
    def __init__(self, 
                 camera: Camera_CS126, 
                 monochromator: MonochromatorControl,
                 focus: Thorlabs.KinesisMotor):
        
        self.camera = camera
        self.mono = monochromator
        self.focus = focus

        # init devices
        self.camera.Init_device()
        self.mono.initialize_arduino()
        # focus is initialized automatically 

    def shutdown(self):
        self.camera.Shutdown_device()
        self.mono.disconnect()
        self.focus.close()

    def __del__(self):
        self.shutdown()

    def set_camera_settings(self,
                            exposure_time: int, 
                            gain: int, 
                            black_level: int, 
                            bit_depth=np.uint16, 
                            out_bit_depth=np.float32) -> None:
        """ Exposure time in ms"""
        self.camera.Set_settings(exposure_time*1000,
                                 gain, black_level, 
                                 bit_depth, out_bit_depth)
        
    



    