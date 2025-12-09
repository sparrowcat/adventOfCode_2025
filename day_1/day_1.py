if __name__ == "__main__":
    # Dial is initally as 50, and we need to count number of times dial hits 0 in the rotations

    dial_pos = 50
    num_zeros = 0
    direction = { "R": 1, "L": -1 }

    with open("dialsequence.txt", "r") as f:
        for line in f:
            multiplier = direction[line[0]]

            dial_pos = (int(line[1:]) * multiplier + dial_pos) % 100

            if dial_pos == 0: num_zeros += 1

    print(num_zeros)

