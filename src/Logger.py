""" @package Logging 

@brief Centralized logging

@details This module defines a global logger used to generate messages about current state of program.
Module is constructed in such a way that importing it sets up logging facilities.
It is expected to be imported exactly once.

Usage example:
@code
  import src/logging
@endcode
"""

# run this once imported
import logging

time_format = '%H:%M:%S'
log_format = '[%(levelname)s] %(asctime)s.%(msecs)03d [%(funcName)s]: %(message)s'
logging.basicConfig(format=log_format, datefmt=time_format)
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)