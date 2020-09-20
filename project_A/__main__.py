
import os 
import sys 
sys.path.append("./")
#
#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#print ( currentframe ) 
#
import sys
#sys.path.insert(0,'..')

import sys
sys.dont_write_bytecode=True



#from lib import getArguments, parseArguments, setup, execute_task, generate_report , mail_report , cleanup
from lib import getArguments, parseArguments, setup, execute_task, mail_report , cleanup
#import dataSetDiff
#import projectAFunctions

#from project_A import project_A 

from project_A import *
#import  project_A.project_A 
#import project_A


if __name__ == "__main__":
    print ("\n**** Main ****\n")

    argumentsObject = getArguments()

    config = parseArguments(argumentsObject)

    # cleanup
    setup(config)

    # execute differ task
    #execute_task("perform_diff",config)
    # execute_project_A_function(config) 
    perform_diff(config) 

    # generate report html and mail
    #generate_report(config)

    # mail report
    #mail_report(config)

    cleanup(config)

