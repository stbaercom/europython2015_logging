import sys, log1, random, logging

task = log1.build_task(10000,1)
log1.load_mem_config()

arg = sys.argv[1]

if arg == "full":
    print("Full Logging")
    log1.division_task_handler(task)
elif arg =="nofunc":
    print("No Logging calls at all")
    log1.division_task_handler_no_log(task)
elif arg == "precallcheck":
    print("Check Logging Lvl before Call, Logging disabled")
    logging.getLogger().setLevel(logging.ERROR)
    log1.division_task_handler_check_lvl(task)
elif arg == "gloaloff":
    print("Logging module level disabled")
    logging.disable(logging.ERROR) # Disable
    log1.division_task_handler(task)
elif arg == "nocall":
    print("disable Caller information")
    logging._srcfile = None
    log1.division_task_handler(task)