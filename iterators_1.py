class SequenceOfNumbers:

    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self

def main():
    print (list(zip(SequenceOfNumbers(), 'abcdef')))

    x = SequenceOfNumbers()
    for i in range(5):
        next(x)
    
    print (x.current)

if __name__ == '__main__':
    main()