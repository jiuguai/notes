import os
import traceback
import logging
import datetime


logger = None


def init_logger(log_dir, pre_name):
    global logger

    if logger is not None:
        for handler in [handler for handler in logger.handlers]:

            logger.removeHandler(handler)

    logger = logging.getLogger()


    logger.setLevel(logging.DEBUG)
    now_s = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    log_path = os.path.join(log_dir, "%s %s.log" %(pre_name, now_s))
    fh = logging.FileHandler(log_path,encoding='utf-8',)
    ch = logging.StreamHandler() 

    formatter = logging.Formatter('%(asctime)s %(filename)s, line - %(lineno)+5s, [%(levelname)s] :  %(message)s')
    
    fh.setLevel(logging.INFO)
    ch.setLevel(logging.DEBUG)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


class GenLogger():
    def __init__(self, log_dir, pre_name, fh_level, ch_level, log_format=None,dt_format='%Y-%m-%d %H_%M_%S'):
        self.pre_name = pre_name
        self.log_dir = log_dir
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        now_s = datetime.datetime.now().strftime(dt_format)
        log_path = os.path.join(log_dir, "%s %s.log" %(pre_name, now_s))
        fh = logging.FileHandler(log_path,encoding='utf-8',)
        ch = logging.StreamHandler() 
        if log_format is None:
            log_format = '%(asctime)s %(filename)s, line - %(lineno)+5s, [%(levelname)s] :  %(message)s'
        formatter = logging.Formatter(log_format)
        fh.setLevel(fh_level)
        ch.setLevel(ch_level)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger

    def __call__(self):
        return slef.logger

def init_logger(log_dir, pre_name):
    global logger

    if logger is not None:
        for handler in [handler for handler in logger.handlers]:

            logger.removeHandler(handler)

    logger = logging.getLogger()


    logger.setLevel(logging.DEBUG)
    now_s = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    log_path = os.path.join(log_dir, "%s %s.log" %(pre_name, now_s))
    fh = logging.FileHandler(log_path,encoding='utf-8',)
    ch = logging.StreamHandler() 

    formatter = logging.Formatter('%(asctime)s %(filename)s, line - %(lineno)+5s, [%(levelname)s] :  %(message)s')
    
    fh.setLevel(logging.INFO)
    ch.setLevel(logging.DEBUG)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


def catch_err(func):
    def inner(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            logger.error("\n %s" %traceback.format_exc())
    return inner

@catch_err
def fun(a, b):
    return a/b


if __name__ == "__main__":
    # log_dir = r"C:\Users\Administrator\Desktop\log"
    # init_logger(log_dir,"jiuguai")
    # fun(1,0)
    # 
    # print("%+8s" %("z"))

    print(__name__)
    a = -1
    print(f"{{  {a:+.2f} }} {{\ }} %s " %('zero') )