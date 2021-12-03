def main():

    with open("input.txt", "r+") as file:
        content = file.readline()

        coordinates = set()
        x = 0
        y = 0

        coordinates.add((x,y))

        for char in content:
            if char == '>':
                x += 1
            if char == '<':
                x -= 1
            if char == 'v':
                y -= 1
            if char == '^':
                y += 1
            coordinates.add((x, y))

        print(coordinates.__len__())


if __name__ == "__main__":
    main()

