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

    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    if string.__contains__("ab") or string.__contains__("cd") or string.__contains__("pq") or string.__contains__("xy"):
        return False

    if contains_three_vowels(string) and contains_letter_twice(string):
        return True

    return False


# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
def contains_three_vowels(string):
    vowels = 'aeiou'
    num_vowels = 0

    for char in string:
        if vowels.__contains__(char):
            num_vowels += 1
        if num_vowels >= 3:
            return True

    return False


# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
def contains_letter_twice(string):

    for i in range(1, string.__len__()):
        if string[i-1] == string[i]:
            return True

    return False


if __name__ == "__main__":
    main()

