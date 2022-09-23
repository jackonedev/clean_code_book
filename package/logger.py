import logging
import os


class Logger:
    path = os.getcwd() + "\data\\"
    os.makedirs(path, exist_ok=True)

    def __init__(self, FILE_NAME):
        self.file_path = self.path + FILE_NAME

    def logginConfig(self):
        formatter = "%(levelname)s:\n\t%(message)s\n%(asctime)s | line %(lineno)d\n"
        logging.basicConfig(
            filename=f"{self.file_path}.log",
            level=logging.INFO,
            force=True,
            filemode="w",
            **{"format": formatter},
        )
        logger = logging.getLogger()
        return logger


def sequence(start=1):
    while True:
        yield start
        start += 1


class Msg:
    path = os.getcwd() + "\data\\"

    def __init__(self, FILE_NAME):
        self.file_path = self.path + FILE_NAME
        self.block = True
        self.x = sequence()

    def set(self, msg):
        return "{}) {}".format(next(self.x), msg)


def buildLogger(FILE_NAME):
    """Funcionamiento buildLogger

    Keyword arguments:
    FILE_NAME:str -- Usa ese nombre para crear FILE_NAME.log y FILE_NAME.enum en la carpeta data del directorio. Si no existe, la crea.
    Return: logger, msg: tuple -- Ambos son instancias de clases, el modo de funcionamiento es el siguiente:
        logger.info(msg.set("Logger information"))

        logger.info(msg.set("var = {}".format(var)))
    """

    logger = Logger(FILE_NAME)
    logger = logger.logginConfig()
    msg = Msg(FILE_NAME)
    return logger, msg


def main():
    logger, msg = buildLogger("Test_7")
    logger.info(msg.set("Haciendo prueba 1"))
    logger.warning(msg.set("Haciendo prueba 2"))
    logger.error(msg.set("Haciendo prueba 3"))
    logger.critical(msg.set("Haciendo prueba 4"))

    obj = "PRUEBA"
    value = "ejemplo"
    logger.info(msg.set(f"setting {obj}.descriptor to {value}"))


if __name__ == "__main__":
    main()
