def main():
    with open("input.txt", "r+") as file:
        content = file.readline()

        coordinates = set()
        santa_x = 0
        santa_y = 0
        robo_x = 0
        robo_y = 0

        coordinates.add((santa_x, santa_y))

        for i, char in enumerate(content):
            if i % 2 == 0:
                if char == '>':
                    santa_x += 1
                if char == '<':
                    santa_x -= 1
                if char == 'v':
                    santa_y -= 1
                if char == '^':
                    santa_y += 1
            else:
                if char == '>':
                    robo_x += 1
                if char == '<':
                    robo_x -= 1
                if char == 'v':
                    robo_y -= 1
                if char == '^':
                    robo_y += 1

            coordinates.add((santa_x, santa_y))
            coordinates.add((robo_x, robo_y))

        print(coordinates.__len__())


if __name__ == "__main__":
    main()

