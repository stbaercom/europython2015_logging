
import json;
import logging;
import logging.config
import logging_tree

logging.config.dictConfig(json.load(open("conf_dict.json")))

log = logging.getLogger("") 
child_A = logging.getLogger("A") 
child_B = logging.getLogger("B") 
child_B_A = logging.getLogger("B.A")

log.info("Now this is %s logging!","good")
child_A.info("Now this is more logging!")
log.warning("Now this is %s logging!","worrisome")

logging_tree.printout()