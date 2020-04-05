import argparse

def getArguments():

    argumentParser = argparse.ArgumentParser(description='Optional app description')

    argumentParser.add_argument('--config','-c', type=str, required=True ,
                        help='config file name argument',
                        default="/tmp/foo.cfg" )

    argumentParser.add_argument('--dataset_one','-b1', type=str,  required=True ,
                        help='dataset one name')

    argumentParser.add_argument('--dataset_two','-b2', type=str,  required=True ,
                        help='dataset two name')

    argumentParser.add_argument('--tag_name','-r', type=str,
                        help='tag for reporting purposes',
                        default="[Test-tag-name not available]" )

    return argumentParser
