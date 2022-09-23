class NumberSequence:

    def __init__(self, start=0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current

def main():
    x = NumberSequence()

    # print (x.current)
    print (x.next())
    print (x.next())
    print (x.current)
    print (x.next())
    print (x.current)
    # print (x.current)

if __name__ == '__main__':
    main()