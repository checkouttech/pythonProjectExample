#from datetime import datetime, timedelta
import os 
from setupLogger import setupLogger

#def setup(config) :
def prepare_system(config) :
    # create output directory
   output_directory = config.get('UNIQUE','output_directory')

   # create output directory
   if not os.path.exists(output_directory):
      os.makedirs(output_directory)

   setupLogger(config)


