def get_joltage(batteries):
    tens_idx = 0
    max_joltage = 0
    len_b = len(batteries)

    while tens_idx < len_b - 1:
        for ones_idx in range(tens_idx + 1, len_b):
            if (ones_idx != len_b - 1) and batteries[ones_idx] > batteries[tens_idx]:
                tens_idx = ones_idx
                break

            max_joltage = max(max_joltage, 10 * batteries[tens_idx] + batteries[ones_idx])

            if ones_idx == len_b - 1:
                return max_joltage

    return max_joltage



if __name__ == "__main__":
    total_joltage = 0

    with open("batteries.txt", "r") as f:
        for batteries in f:
            total_joltage += get_joltage([int(b) for b in batteries.strip()])

    print(total_joltage)

