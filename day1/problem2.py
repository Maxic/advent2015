def main():
    with open("input.txt", "r+") as file:
        content = file.readline()

        floor = 0
        position = 1
        for instruction in content:
            if instruction == '(':
                floor += 1
            elif instruction == ')':
                floor -= 1

            if floor == -1:
                break
            position += 1

        print(position)


if __name__ == "__main__":
    main()

