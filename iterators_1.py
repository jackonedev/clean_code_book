# Iterators and Generators
# pag-272-.pdf


def sequence(start=0):
    while True:
        yield start
        start += 1


def main():

    print(list(zip(sequence(), "abcdef")))

    x = sequence()
    print(type(x))

    print(next(x))
    print(next(x))
    print(next(x))


if __name__ == "__main__":
    main()
