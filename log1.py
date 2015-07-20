import logging
import logging.config
import json
import traceback
import re
import random

def load_config(enable_console=True):
    file_config = json.load(open("conf_dict_with_file.json"))
    file_config['handlers']['console']['level'] = logging.ERROR
    logging.config.dictConfig(file_config)


def load_mem_config():
    file_config = json.load(open("conf_dict_with_mem.json"))
    logging.config.dictConfig(file_config)

def simple1():
    logging.debug("Debug!")
    logging.info("Info!")
    logging.warning("Warning!")
    logging.error("Error")
    logging.critical("Critical")
    try:
        0/0
    except ZeroDivisionError:
        logging.exception("Exception!")

def simple2():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logger.debug("Debug!")
    logger.info("Info!")
    logger.warning("Warning!")
    logger.error("Error")
    logger.critical("Critical")

def example():
    logger = logging.getLogger(__name__) ## LC

def build_task(length, seed):
    random.seed(seed)
    v = lambda : (random.random() - 0.5) * 100.0
    result = [(v(),v()) for i in range(length)]
    return result

def my_division(dividend, divisor):
    try:
        log.debug("Division : %s/%s", dividend, divisor)
        result = dividend / divisor
        return result
    except (ZeroDivisionError, TypeError):
        log.exception("Error, Division Failed")
        return None

def division_task_handler(task):
    log.info("Handling division task,%s items",len(task))
    result = []
    for i, task in enumerate(task):
        log.info("Doing devision iteration %s",i)
        dividend, divisor = task
        result.append(my_division(dividend,divisor))
    return result
    
def my_division_no_log(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except (ZeroDivisionError, TypeError):
        return None

def division_task_handler_no_log(task):
    result = []
    for i, task in enumerate(task):
        dividend, divisor = task
        result.append(my_division_no_log(dividend,divisor))
    return result
    
def my_division_check_lvl(dividend, divisor):
    try:
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Division : %s/%s", dividend, divisor)
        result = dividend / divisor
        return result
    except (ZeroDivisionError, TypeError):
        if log.isEnabledFor(logging.ERROR):
            log.exception("Error, Division Failed")
        return None

def division_task_handler_check_lvl(task):
    if log.isEnabledFor(logging.INFO):
        log.info("Handling division task,%s items",len(task))
    result = []
    for i, task in enumerate(task):
        if log.isEnabledFor(logging.INFO):
            log.info("Doing devision iteration %s",i)
        dividend, divisor = task
        result.append(my_division_check_lvl(dividend,divisor))
    return result
    
def get_clean_logging():
    import sys
    import logging
    logging.shutdown()
    if sys.version[0] == "2":
        return reload(logging)
    else:
        import importlib
        return importlib.reload(logging)

class JSONFormatter(logging.Formatter):
    def __init__(self,multiline = False):
        if multiline == True:
            self.separators = (',\n', ':')
        else:
            self.separators = (',', ': ')
        super(JSONFormatter, self).__init__()

    def format(self, record):
        vals = {}
        for k,v in record.__dict__.items():
            if v is not None:
                if k == "exc_info":
                    trace = traceback.format_exception(v[0],v[1],v[2])
                    trace  = "|".join(t for t in trace)
                    vals[k] = re.sub(r'''[\s"']+'''," ",trace)
                else:
                    vals[k] = v
        return json.dumps(vals, separators = self.separators)


load_mem_config()
log = logging.getLogger()
