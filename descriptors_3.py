# Descriptors pag-235.pdf Data Descriptors
from package.logger import *

logger, msg = buildLogger('descriptors_3')

class DataDescriptor:

    def __init__(self):
        self._name = None

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return 42

    def __set_name__(self, objtype, name):
        self._name = name

    def __set__(self, obj, value):
        logger.info(msg.set(f"setting {obj}.descriptor to {value}"))
        obj.__dict__[self._name] = value

class ClientClass:
    descriptor = DataDescriptor()


def main():
    client = ClientClass()
    client.descriptor
    print (client.descriptor)

    client.descriptor = 99
    print (client.descriptor)

    print (vars(client))
    print (client.__dict__["descriptor"])


if __name__ == '__main__':
    main()