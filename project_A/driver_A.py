import os 
import sys 
sys.path.append("./")
sys.dont_write_bytecode=True

#from lib import getArguments, parseArguments, setup, execute_task, mail_report , cleanup
from lib import getArguments, parseArguments, prepare_system, execute_task, mail_report , cleanup
# need to add generate report method 

from project_A import *

if __name__ == "__main__":
    print ("\n**** Main ****\n")

    # get all input arguments 
    argumentsObject = getArguments()

    # get configuration object 
    config = parseArguments(argumentsObject)

    # cleanup
    prepare_system(config)

    # execute differ task
    #execute_task("perform_diff",config)
    perform_diff(config) 

    # generate report html and mail
    #generate_report(config)

    # mail report
    #mail_report(config)

    # perform cleanup 
    cleanup(config)

