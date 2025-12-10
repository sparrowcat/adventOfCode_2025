from math import log10

def parse_ranges(r):
    """
    return a list of tuples, each tuple representing an ID range
    """
    return [tuple(int(i) for i in ids.split('-')) for ids in r.split(',')]


def find_invalid_twice_repeated(lower, upper):
    """
     find invalid IDs between a lower and upper bound, inclusive
     returns a list of invalid IDs if invalid IDs have the same sequence
     of numbers repeated TWICE in the number, eg 123123
     """

    invalid = []
    for i in range(lower, upper + 1):
        # based on problem description, it does not seem that any
        # IDs in ranges will be 0 or negative

        # if there is an even number of digits
        numlen = int(log10(i)) + 1
        if (numlen % 2 == 0):
            half_numlen = numlen // 2
            # and if the first half of the digits is the same as the back half...
            if (i // (10 ** half_numlen) == i % (10 ** half_numlen)):
                invalid.append(i)
    return invalid


def find_any_invalid(lower, upper):
    """
    same as above; finds invalid IDs between lower and upper ranges, inclusive
    returns a list of invalid IDs
    now, invalid IDs can have a sequence of digits repeating any number of times > 1
    eg: 1212121212, 123123123
    """

    invalid = []
    for i in range(lower, upper + 1):
        id_string = str(i)
        id_len = len(id_string)
        for l in range(1, (id_len//2) + 1):
            if (id_len / l == id_len // l) and (id_string[:(l)] * (id_len // l) == id_string):
                invalid.append(i)
                break
    return invalid



if __name__ == "__main__":
    # ranges appear in a single line
    with open("ranges.txt", "r") as f:
        ranges_string = f.readlines()[0]

    double_invalid = [] 
    all_invalid = []
    ranges = parse_ranges(ranges_string)
    for r in ranges:
        double_invalid += find_invalid_twice_repeated(r[0], r[1])
        all_invalid += find_any_invalid(r[0], r[1])

    print(sum(double_invalid))
    print(sum(all_invalid))

    
