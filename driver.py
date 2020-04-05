
from lib import getArguments, parseArguments, setup, execute_task, generate_report , mail_report , cleanup
import dataSetDiff

if __name__ == "__main__":
    print ("\n**** Main ****\n")

    argumentsObject = getArguments()

    config = parseArguments(argumentsObject)

    # cleanup
    setup(config)

    # execute differ task
    #execute_task("perform_diff",config)

    # generate report html and mail
    generate_report(config)

    # mail report
    mail_report(config)

    cleanup(config)

