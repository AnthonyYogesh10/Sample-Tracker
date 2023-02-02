import inspect
import logging

class utils():
    def custom_logger(self,mode):
        #set class or method name from where it is called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(level=logging.DEBUG)
        # create console handler or file handler
        fh = logging.FileHandler(filename="automation.log",mode= mode)
        # add formatter to console or file handler
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s', datefmt='%d-%b-%y %H:%M:%S')
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console handller to logger
        logger.addHandler(fh)
        return logger





# utlities are used to set common things which not related with driver
# base module are used to set common things which are related with driver
