#from datetime import datetime, timedelta
import os 
from setupLogger import setupLogger

def setup(config) :
    # create output directory
   output_directory = config.get('UNIQUE','output_directory')

   # create output directory
   if not os.path.exists(output_directory):
      os.makedirs(output_directory)

#   html_output_directory = arguments['output_directory'] +"/html/"
#    cmd_create_html_output_directory = " mkdir -p "+ html_output_directory
#    logger.info cmd_create_html_output_directory
#    os.system ( cmd_create_html_output_directory )


   setupLogger(config)


