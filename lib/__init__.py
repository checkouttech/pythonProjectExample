import argparse
import ConfigParser
from datetime import datetime, timedelta
import datetime
import ConfigParser
import os 
import json 

from getArguments import getArguments 
from parseArguments import parseArguments
from setup import setup 
from execute_task import execute_task
from setupLogger import setupLogger
#from generate_report import generate_report
#from generate_report_summary import generate_report_summary
#from generate_report_details import generate_report_details
#from mail_report import mail_report 
from cleanup import cleanup 

import sys
sys.dont_write_bytecode=True


global logger

def packA_func():
    print("running packA_func()")



