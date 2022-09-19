# Descriptors pag-235.pdf Data Descriptors
from package import *
from package.logger import buildLogger
import logging

logger, msg = buildLogger('descriptors_3')

class DataDescriptor:

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return 42

    def __set__(self, obj, value):
        logger.info(msg.set(f"setting {obj}.descriptor to {value}"))
        obj.__dict__["descriptor"] = value

class ClientClass:
    descriptor = DataDescriptor()


def main():
    client = ClientClass()
    client.descriptor = 43
    print (client.descriptor)


if __name__ == '__main__':
    main()