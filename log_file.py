import logging

def setup_logging(script_name):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler for the script
    handler = logging.FileHandler(f'C:\\Users\\DELL\\Downloads\\9_30_Ml_P\\credit_card\\logs\\{script_name}.log', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
