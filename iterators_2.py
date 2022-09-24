# Iterators and Generators
# pag-275-.pdf

from package.logger import buildLogger

logger, msg = buildLogger("iterator_2")

def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell

def search_nested(array, desired_value):
    try:
        # # # # # # # # # # # # # # # # # # # # # # # # #
        coord = next(
            coord
            for (coord, cell) in _iterate_array2d(array)
            if cell == desired_value
        )
        # # # # # # # # # # # # # # # # # # # # # # # # #
    except StopIteration as e:
        raise ValueError(f"{desired_value} not found") from e
    
    logger.info(msg.set("value {} found at [{}]".format(desired_value, coord)))
    return coord


def main():
    array = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    desired_value = "H"
    coord = search_nested(array, desired_value)

    print (coord)


if __name__ == "__main__":
    main()