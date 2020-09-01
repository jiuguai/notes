import os
import logging
import traceback


log_dir = r"C:\Users\Administrator\Desktop\log"
logger = logging.getLogger('logger')

log_path = os.path.join(log_dir, "LOG1.log")
fh = logging.FileHandler(log_path,encoding='utf-8')


# formatter = logging.Formatter('%(asctime)s %(filename)s [%(lineno)s] - %(levelname)s : %(threadName)s: %(message)s')
formatter = logging.Formatter('%(asctime)s %(filename)s, line - %(lineno)+5s, %(levelname)-8s :  %(message)s')

logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter) 
logger.addHandler(fh)


fh.setLevel(logging.INFO)

logger.addHandler(ch)


print(logger.handlers)
# for handler in [handler for handler in logger.handlers]:
#     print(handler)
#     print(handler in logger.handlers)
#     logger.removeHandler(handler)


print(logger.handlers)
logger.debug('logger debug message')  
logger.info('logger info message')
logger.critical('logger critical message')
# s = traceback.format_exc()






# try:
#     1/0
# except Exception as e:
#     print(str(e))
#     # print("traceback.print_exc()" ,traceback.print_exc())
#     # exc_type, exc_value, exc_traceback = sys.exc_info()
#     # print("exc_type", exc_type)
#     # print("exc_value", exc_value)
#     # s = traceback.print_tb( exc_traceback)

#     # print("exc_traceback", s)
#     # print("sys.exc_info()" ,sys.exc_info())
    

#     logger.info("\n %s" %traceback.format_exc()) 
#     logger.info("\n %s" %traceback.format_exc()) 
# print('zero')