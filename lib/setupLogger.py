import os 
import logging

def setupLogger(config):

   log_directory = config.get('UNIQUE','log_directory')
   log_filename  = config.get('UNIQUE','log_filename')

   if not os.path.exists(log_directory):
      os.makedirs(log_directory)

   FORMAT = '[%(asctime)s %(levelname)s] {%(pathname)s:%(lineno)d} - %(message)s'

   global logger
   logger = logging.getLogger("debug_log")
   logger.setLevel(logging.INFO)
   handler =   logging.FileHandler(log_directory +"/"+ log_filename )
   formatter = logging.Formatter(FORMAT)
   handler.setFormatter(formatter)

   # TODO : add format and level in conf file
   #     # create console handler and set level to info
   #     handler.setLevel(logging.getLevelName(debug_log_level))

   logger.addHandler(handler)
   logger.info("hello info")
   logger.debug("hello debug")
   logger.error("hello error")

