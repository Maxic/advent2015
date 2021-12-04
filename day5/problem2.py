def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

        strings = [line.strip('\n') for line in content]

        num_nice_strings = 0

        for string in strings:
            if is_nice(string):
                num_nice_strings += 1

        print(num_nice_strings)


def is_nice(string):
    if has_two_not_overlapping_pairs(string) and has_duplicate_char_with_separation(string):
        return True
    return False


def has_two_not_overlapping_pairs(string):
    # It contains a pair of any two letters that appears at least twice in the string without overlapping,
    # like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    pairs = []
    for i in range(1, string.__len__()):
        new_pair = string[i-1] + string[i]
        for pair in pairs[:-1]:
            if pair == new_pair:
                return True
        pairs.append(new_pair)

    return False


def has_duplicate_char_with_separation(string):
    # It contains at least one letter which repeats with exactly one letter between them,
    # like xyx, abcdefeghi (efe), or even aaa.
    for i in range(2, string.__len__()):
        if string[i-2] == string[i]:
            return True
    return False


if __name__ == "__main__":
    main()
