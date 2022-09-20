import logging
import datetime as dt
import os

class Logger:
    path = os.getcwd() + '\data\\' 
    os.makedirs(path, exist_ok=True)
    
    def __init__(self, FILE_NAME):
        self.file_path = self.path + FILE_NAME

    def logginConfig(self):
        formatter = '%(levelname)s:\n\t%(message)s\n%(asctime)s | line %(lineno)d\n'
        logging.basicConfig(filename=f'{self.file_path}.log', level=logging.INFO, force=True, filemode='w', **{'format':formatter})
        logger = logging.getLogger()
        return logger


class Msg:
    path = os.getcwd() + '\data\\'
    
    def __init__(self, FILE_NAME):
        self.file_path = self.path + FILE_NAME
        self.block = True

    def set(self, msg):
        return "{}) {}".format(self.x(), msg)

    def x(self):
        try:
            if self.block: 1/0
            with open(f'{self.file_path}.enum', 'r') as file:
                i = file.read()
            i = str(int(i) + 1)
            with open(f'{self.file_path}.enum', 'w') as file:
                file.write(i)
            return i
        
        except:
            with open(f'{self.file_path}.enum', 'a') as file:
                pass
            with open(f'{self.file_path}.enum', 'w') as file:
                file.write('1')
            self.block = False
            return '1'


def buildLogger(FILE_NAME):
    logger = Logger(FILE_NAME)  
    logger = logger.logginConfig()
    msg = Msg(FILE_NAME)
    return logger, msg


def main():
    logger, msg = buildLogger('Test_5')
    logger.info(msg.set('Haciendo prueba 1'))
    logger.warning(msg.set('Haciendo prueba 2'))
    logger.error(msg.set('Haciendo prueba 3'))
    logger.critical(msg.set('Haciendo prueba 4'))

    obj = 'PRUEBA'
    value = 'ejemplo'
    logger.info(msg.set(f"setting {obj}.descriptor to {value}"))

if __name__ == '__main__':
    main()