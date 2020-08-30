import datetime
from random import randint
#import ConfigParser
import configparser 


def parseArguments(arguments):

    id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + str(randint(0, 9))
    #id = "20181008_164133_9"

    #config = ConfigParser.SafeConfigParser()
    #config = configparser.BasicInterpolation() 
    config = configparser.ConfigParser() 

    args = arguments.parse_args()

    if args.config:
        #config = ConfigParser.SafeConfigParser()
        #config = configparser.BasicInterpolation() 
        config = configparser.ConfigParser() 
        config.read([args.config])
    else :
       logger.info ( "no file given")
       sys.exit("no conf file given")

    # add passed params
    for arg in vars(args):
        config.set('UNIQUE',arg, getattr(args, arg) )

    # replace __ID__ with id
    for section in config.sections():
        #for option in config.items(section):
        for option in config.options(section):
            print ( str(section) + " -- " + str(option) )
            print ( config.get(section,option) )
            config.set(section,option, config.get(section,option).replace("__ID__",id) )
            config.set(section,option, config.get(section,option).replace("TAG_NAME", config.get('UNIQUE','tag_name')))
            print ( config.get(section,option))


    #defaults.update({k: arguments[k] for k in arguments if arguments[k] is not None  })
    return ( config )




