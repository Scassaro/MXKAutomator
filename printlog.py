import logging

def setuplog(filestring):
    logging.basicConfig(filename=filestring, setLevel=DEBUG)
    return

def printandlog(printlogstring):
    logging.debug(printlogstring)
    logging.debug("<br>")
    print(printlogstring)
    return
