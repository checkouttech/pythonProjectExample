import os 
import logging 


def getDatasetDetails(config):

    #logger = logging.getLogger(__name__)
    logger = logging.getLogger("debug_log") 
    something = "this is inside getDatasetDetails "
    logger.info("I am warning you about %s", something)



    # get datase  one details
    cmd_get_dataset_one_location = "echo  " \
                                       + config.get('UNIQUE','dataset_one')  \
                                       + " "

    logger.info ( cmd_get_dataset_one_location ) 

    try :
        dataset_one_location = os.popen(cmd_get_dataset_one_location).read().split()[0]
    except AttributeError :
        dataset_one_location = "unknown"

    config.set('UNIQUE','dataset_one_location', dataset_one_location )

    print ( "dataset_one_location --------  :" , dataset_one_location ) 





    # get dataset two details
    cmd_get_dataset_two_location = "echo  " \
                                       + config.get('UNIQUE','dataset_two')  \
                                       + " "

    logger.info ( cmd_get_dataset_two_location ) 

    try :
        dataset_two_location = os.popen(cmd_get_dataset_two_location).read().split()[0]
    except AttributeError :
        dataset_two_location = "unknown"

    config.set('UNIQUE','dataset_two_location', dataset_two_location )

    print ( "dataset_two_location --------  :" , dataset_two_location ) 









