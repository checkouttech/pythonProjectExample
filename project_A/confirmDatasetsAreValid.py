import logging 


def confirmDatasetsAreValid (config):

    # confirm if dataset one exists , exit if yes
    # confirm if dateset two exists , exit if yes

    logger = logging.getLogger("debug_log") 
    logger.info("start ")

    cmd_confim_dataset_one_exits = " echo \
                                   " + config.get('UNIQUE','dataset_one')  

    cmd_confim_dataset_two_exits = " echo \
                                   " + config.get('UNIQUE','dataset_two')  

    logger.info ( cmd_confim_dataset_one_exits  )
    # check if dataset one exists 


    # confim if dataset one and two are same , exit if yes
    if config.get('UNIQUE','dataset_one') == config.get('UNIQUE','dataset_two') :
       logger.error ("both datasets are same")
       sys.exit ("both datasets are same " )





