
from confirmDatasetsAreValid import confirmDatasetsAreValid
from getDatasetDetails import getDatasetDetails

import logging 
import os 
import json 
import subprocess
import sys


import logging




def perform_diff(config):
    logger = logging.getLogger("debug_log") 

    confirmDatasetsAreValid(config)
    getDatasetDetails(config)

    # create output location

    # run differ cmd 
    logger.info ("\n**** Perform Diff **** \n" )

    types =  json.loads(config.get('UNIQUE','types'))
    for type_name in types :
       logger.info ( type_name  )


       print ( "\n\n\n " +  type_name + "  \n\n\n " ) 

       print ( config.get('UNIQUE','perform_diff_script') ) 

       perform_diff_script =  config.get('UNIQUE','perform_diff_script').replace("__TYPE_NAME__", type_name )
       logger.info ( perform_diff_script ) 

       perform_diff_output_directory =  config.get('UNIQUE','perform_diff_output_directory').replace("__TYPE-NAME__", type_name )
       logger.info ( perform_diff_output_directory)

       print ( perform_diff_output_directory ) 


       cmd_perform_diff = "echo " \
                                " -f "+ perform_diff_script +  \
                                " -d "+ perform_diff_output_directory   
       logger.info ( cmd_perform_diff )

       try :
           #os.system( cmd_type_perform_diff_insert_result )
           subprocess.check_call(cmd_perform_diff, shell=True )
       #except :
       except Exception, e :
           logger.error("issue with running the command " + cmd_perform_diff )
           logger.error(e)

           output_directory = config.get('UNIQUE','output_directory')

           error_message =  (
                            "Subject : DeepDiff Error \n"
                            "Content-Type: text/html \n"
                            "{od}/logs/debug.log\n"
                            "."
                            ).format(od=output_directory)

           with open( output_directory + "/error.html", 'w') as f:
                f.write(error_message)

           cmd_mail_error_alert = "/usr/sbin/sendmail " + config.get('UNIQUE','error_alert_email_id') + " < "+ output_directory + "/error.html"
           subprocess.check_call(cmd_mail_error_alert, shell=True )
           sys.exit ("issue with running the command " + cmd_type_perform_diff_insert_result )




