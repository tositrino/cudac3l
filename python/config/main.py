"""
main.py - main config 

"""

import os

# APP standard variables

APP_VERNAME = "cudac3l"
APP_VERID = "0.1.0"
APP_VERINFO = "cuda.cccl tests"
APP_RELDATE = "2025/07/21"
APP_RELINFO = "first!"
APP_COPYRIGHT = "copyright (c) 2025 by development at ths dot one"
APP_LICENSE = "GPL3"
APP_LICENSEINFO = "please see ./LICENSE file in the main directory for further info"
APP_WARRANTY = "this software comes with absolutely no warranties whatsoever"
APP_NODEID = 0x4343434E  # "CCCL" 

# control variables

# debug level and threshold
debug_level: int = 0
debug_threshold: int = 1
# verbose level and threshold
verbose_level: int = 1
verbose_threshold: int = 1
# force mode (overwrite existing files)
force_mode: bool = False
# cleanmode (clear all files before writing to them (do not append)
clean_mode: bool = True

logging: bool = True
log_level = None
log_directory = "../intermediate_data/logs"
log_file_name = "${APP_VERNAME}.log"
log_file_mode = "w"

max_errors = 1
error_count = 0
error_messages = []
max_warnings = 0
warn_count = 0
warn_messages = []
force_return_code = 0
return_code = 0
atexit_list = []
in_termination = 0

# environment file (loaded with dotenv)
env_file = f"~/lsr/etc/env/{APP_VERNAME}.env"

# directory settings
data_directory = "../data"

# import all other configs here
import config.c3l as c3l

# end of main config
