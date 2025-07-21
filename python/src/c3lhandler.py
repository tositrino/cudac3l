"""
c3lhandler - class to handle cuda.cccl functions
"""

# standard includes
import datetime
import logging
import os
import re
import sys
import time

# torch
import torch
import torchvision
import torchaudio

# module configs
import config.main as config

# local modules
import src.errorhandler as eh

# c3l handler class
# this class handles the cuda.cccl calls

class C3lHandler:
    def __init__(
        self,
        work_dir=config.c3l.work_directory,
        result_dir=config.c3l.result_directory,
        vblth=config.verbose_threshold,
        dblth=config.debug_threshold,
    ):
        self.class_name = "C3lHandler"
        self.work_directory = work_dir
        self.result_dir = result_dir
        self.vblth = vblth
        self.dblth = dblth

    def tests(self)->int:
        """run cccl tests"""
        method_name = "tests"
        method_start = time.time()
        method_status = 0
        eh.verbose_print(
            self.vblth,
            f"{self.class_name}.{method_name} - running cccl tests",end=""
        )
        cuda_available = torch.cuda.is_available()
        if not cuda_available:
          method_status = -1
          eh.verbose_print( self.vblth," ... [CUDA is not available, aborted]")
        else:
          eh.verbose_print(self.vblth,":")
          eh.verbose_print(
                    self.vblth,
                    f"{self.class_name}.{method_name} - dummy test ... ",
                    end="",
                )
          time.sleep(2)
          eh.verbose_print(self.vblth,"[done")
        method_elapsed = time.time() - method_start
        eh.verbose_print(
            1,
            f"{self.class_name}.{method_name} - finished, duration={method_elapsed:2.4f} second(s), status={method_status}:",
        )
        return method_status
