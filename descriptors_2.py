# Descriptors pag-233 Non-Data Descriptors

class NonDataDescriptor:
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return 42

class ClientClass:
    descriptor = NonDataDescriptor()


def main():
    client = ClientClass()
    print (client.descriptor)
    client.descriptor = 43
    print (client.descriptor)
    del client.descriptor
    print (client.descriptor)
    print (vars(client))
    client.descriptor = 99
    print (vars(client))
    del client.descriptor
    print (client.descriptor)
    print (vars(client))

if __name__ == '__main__':
    main()