import sys 


def cleanup(config):
    output_directory = config.get('UNIQUE','output_directory')
    with open( output_directory + '/config.ini', 'w') as configfile:
         config.write(configfile)
    sys.exit()



