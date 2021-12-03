def main():

    with open("input.txt", "r+") as file:
        content = file.readline()

        floor = 0

        for instruction in content:
            if instruction == '(':
                floor += 1
            elif instruction == ')':
                floor -= 1

        print(floor)


if __name__ == "__main__":
    main()

