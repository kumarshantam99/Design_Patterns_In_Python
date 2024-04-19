DEBUG='debug'
INFO='info'
WARNING='warning'
ERROR='error'

class Logger:

    def __init__(self,name):
        print('Logger initialized:',name)

    def log(self, message):
        print('Logging to some output')

class __ConsoleLogger(Logger): # Private implementation

    def __init__(self,name):
        Logger.__init__(self,name)

    def log(self, message):
        print('Logging in console',message)

class __FileLogger(Logger): # Private implementation

    def __init__(self,name):
        Logger.__init__(self,name)

    def log(self, message):
        print('Logging in file',message)

CONSOLE_LOGGER=__ConsoleLogger('console')
FILE_LOGGER=__FileLogger('file')