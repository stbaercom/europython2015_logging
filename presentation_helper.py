import ipy_table

def customize_settings():
    from IPython.display import display, HTML
    from IPython.html.services.config import ConfigManager
    from IPython.utils.path import locate_profile
    cm = ConfigManager(profile_dir=locate_profile(get_ipython().profile))
    cm.update('livereveal', {'width': 1024,'height': 768,})
    display(HTML(open("notebook_style.css").read()))

attr= [
["Attribute",  "Description"],
["args","Tuple of arguments passed to the logging call"],
["asctime", "Log record creation time, formatted"],
["created", "Log record creation time, seconds since  the Epoch"],
["exc_info", "Exception information / stack trace, if any"],
["filename", "Filename portion of pathname for the logging module"],
["funcName",  "Name of function containing the logging call"],
["levelname",  "Name of Logging Level"],
["levelno", "Number of Logging Level"],
["lineno","Line number in source code for the logging call"],
["module", "Module (name portion of filename)."],
["message", "Logged message"],
["name" ,"Name of the logger used to log the call."],
["pathname","pathname of source file"],
["process","Process ID"],
["processName","Process name"],
["thread","Thread ID"],
["threadName","Thread name"]]


attr2 = [
["Logging Aspects","Question","Description"],
["Severity","How Important?","Log Level: DEBUG, INFO, WARN, ERROR, CRITICAL"],
["Origin/Logger","Where?","Logger Name: ROOT, module name, etc..."],
["Context","When?","Technical attributes, set by the logging library (time, module,...) and manual defined context (session, ...)"],
["Message","What?","Combination of text, attributes and context"],
["Format","How does it look like?","Template to build message "],
["Select / Route","Who should know?","What gets send to which handler"],
["Destination","How do we store/send/show it?","To what file, mail, socket, aggregator are the messages sent?"]
]

bench = [
    ["Scenario (10000 Call, 3 Logs per call)","Runtime"],
    ["Full Logging with buffered writes", "3.096s"],
    ["Disable Caller information", "2.868s"],
    ["Check Logging Lvl before Call, Logging disabled", "0.186s"],
    ["Logging module level disabled", "0.181s"],
    ["No Logging calls at all", "0.157s"]
]



def build_table(data):
    acum = []
    aa = acum.append
    aa('<table class="bst"><tr>')
    for c in data[0]:
        aa('<th>%s</th>' % c)
    aa("</tr>")
    for i,r in enumerate(data[1:]):
        aa("<tr>")
        for c in r:
            aa('<td>%s</td>' % c)
        aa("</tr>")
    aa("</table>")
    return "".join(acum)
