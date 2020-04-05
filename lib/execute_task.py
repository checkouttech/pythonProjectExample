import sys 
from dataSetDiff.perform_diff import perform_diff


def execute_task(task_function, config) :

   #try:
   #    return importlib.import_module(function)
   #except ImportError as err:
   #    logger.info('Error:', err)

   #module_name = 'yoursubfile'
   #function_name = 'foo_func'
   #argument_name = "this is an argument"

   current_module = sys.modules[__name__]
   
   print ( "current_module" ) 
   print ( current_module ) 
   getattr(current_module,task_function)(config)



