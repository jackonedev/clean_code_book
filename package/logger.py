import logging
import datetime as dt
import os

class Logger:
    path = os.getcwd() + '\data\\' 
    os.makedirs(path, exist_ok=True)
    
    def __init__(self, FILE_NAME):
        self.file_path = self.path + FILE_NAME

    def logginConfig(self):
        formatter = '%(levelname)s:\n %(message)s \n%(asctime)s| line %(lineno)d\n'
        logging.basicConfig(filename=f'{self.file_path}.log', level=logging.INFO, force=True, filemode='w', **{'format':formatter})
        logger = logging.getLogger()
        return logger


class Msg:
    path = os.getcwd() + '\data\\'
    
    def __init__(self, FILE_NAME):
        self.file_path = self.path + FILE_NAME

    def set(self, msg):
        return "{}) {}".format(x(FILE_NAME=self.file_path), msg)

block = True
def x(*, FILE_NAME):
    global block
    try:
        if block: 1/0
        with open(f'{FILE_NAME}.enum', 'r') as file:
            i = file.read()
        i = str(int(i) + 1)
        with open(f'{FILE_NAME}.enum', 'w') as file:
            file.write(i)
        return i
    
    except:
        with open(f'{FILE_NAME}.enum', 'a') as file:
            pass
        with open(f'{FILE_NAME}.enum', 'w') as file:
            file.write('1')
        block = False
        return '1'


def main():
    FILE_NAME = 'Test_3'
    logger = Logger(FILE_NAME)  
    logger = logger.logginConfig()
    msg = Msg(FILE_NAME)
    logger.info(msg.set(msg='Haciendo prueba 1'))
    logger.info(msg.set(msg='Haciendo prueba 2'))
    logger.info(msg.set(msg='Haciendo prueba 3'))


if __name__ == '__main__':
    main()