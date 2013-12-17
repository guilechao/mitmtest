import json
import logging
import os
import sys
import traceback
import random
import datetime


request_log_path = "./request.log"
response_log_path = "./response.log"
debug_log_path = "./mitm_debug.log"
if os.path.isfile(request_log_path):os.unlink(request_log_path)
if os.path.isfile(response_log_path):os.unlink(response_log_path)
if os.path.isfile(debug_log_path):os.unlink(debug_log_path)

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)  

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter1 = logging.Formatter("%(levelname)s - %(message)s")
ch.setFormatter(formatter1)
fh = logging.FileHandler(debug_log_path)
fh.setLevel(logging.DEBUG)
formatter2 = logging.Formatter("%(asctime)s %(filename)s %(levelname)s - %(message)s")
fh.setFormatter(formatter2)
logger.addHandler(ch)
logger.addHandler(fh)


def start(ScriptContext):

    try:
        logger.debug("'start' event start")



        logger.debug("'start' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'start', exception_str)


def response(context, flow):

    #use command 'pydoc libmproxy.flow.Response' in terminal to view the help

    try:
        logger.debug("'response' event start")

        response_content = ''
        response_content += '------------------------------------------------------------------------------------\n'

        response_content += 'current time : %s\n' % (str(datetime.datetime.now()))
        response_content += 'code         : %s\n' % (flow.response.code)
        response_content += 'msg          : %s\n' % (flow.response.msg)

        #add this header in response
        flow.response.headers["X-SDET-MITM-RANDOMID"] = [str(random.randint(1, 100000))]

        headers_str = ""
        for h in flow.response.headers:
            headers_str += '    %s : %s\n' % (h[0], h[1])            
        response_content += 'headers : \n%s\n' % (headers_str)
        
        response_content += 'content : \n%s\n' % (flow.response.content)

        response_content += '------------------------------------------------------------------------------------\n'

        open(response_log_path, 'a').write(response_content)

        logger.debug("'response' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'response', exception_str)

def request(context, flow):

    #use command 'pydoc libmproxy.flow.Request' in terminal to view the help

    try:
        logger.debug("'request' event start")

        request_content = ''
        request_content += '------------------------------------------------------------------------------------\n'

        request_content += 'current time : %s\n' % (str(datetime.datetime.now()))
        request_content += 'scheme       : %s\n' % (flow.request.scheme)
        request_content += 'host         : %s\n' % (flow.request.host)
        request_content += 'port         : %s\n' % (flow.request.port)
        request_content += 'path         : %s\n' % (flow.request.path)
        request_content += 'method       : %s\n' % (flow.request.method)

        #add this header in request
        flow.request.headers["X-SDET-MITM-RANDOMID"] = [str(random.randint(1, 100000))]

        headers_str = ""
        for h in flow.request.headers:
            headers_str += '    %s : %s\n' % (h[0], h[1])            
        request_content += 'headers : \n%s\n' % (headers_str)
        
        request_content += 'content : \n%s\n' % (flow.request.content)

        request_content += '------------------------------------------------------------------------------------\n'

        open(request_log_path, 'a').write(request_content)

        logger.debug("'request' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'request', exception_str)

def clientconnect(ScriptContext):

    try:
        logger.debug("'clientconnect' event start")


        logger.debug("'clientconnect' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'clientconnect', exception_str)

def clientdisconnect(ScriptContext, ClientDisconnect):

    try:
        logger.debug("'clientdisconnect' event start")



        logger.debug("'clientdisconnect' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'clientdisconnect', exception_str)

def error(ScriptContext, Flow):

    try:
        logger.debug("'error' event start")



        logger.debug("'error' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'error', exception_str)

def done(ScriptContext):

    try:
        logger.debug("'done' event start")



        logger.debug("'done' event finish")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        exception_str = ''.join('!! ' + line for line in lines)           
        logger.error("exception happen in '%s' event, detail message is \n%s", 'done', exception_str)