import logging
import inspect
import os


def custom_logger(log_level=logging.DEBUG):

    # Get the name of the module where this method is called
    caller_frame = inspect.stack()[1]
    module_name = caller_frame[0].f_globals['__name__']

    # Get the name of the calling function
    calling_function_name = caller_frame[3]

    # Check if the calling function is "<module>" and exclude it
    if calling_function_name == "<module>":
        logger_name = module_name
    else:
        # Get the name of the class where the calling function is defined
        calling_class_name = None
        try:
            # Get the calling frame's locals
            calling_locals = caller_frame[0].f_locals
            # Check for '__class__' in locals to identify the class
            if '__class__' in calling_locals:
                calling_class_name = calling_locals['__class__'].__name__
        except Exception as e:
            print(e)

        # Construct the logger name including class hierarchy
        if calling_class_name:
            logger_name = f"{module_name}.{calling_class_name}.{calling_function_name}"
        else:
            logger_name = f"{module_name}.{calling_function_name}"

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    current_dir = os.path.dirname(os.path.abspath(inspect.stack()[1].filename))
    project_dir = os.path.dirname(current_dir)
    log_file_path = os.path.join(project_dir, 'results', 'automation.log')
    file_handler = logging.FileHandler(log_file_path, mode='a')

    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
