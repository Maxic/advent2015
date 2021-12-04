def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip('\n') for line in content]

        instructions = []

        # Parse input and get instructions
        for line in line_arr:
            command = None
            if line.startswith("turn on "):
                line = line.replace("turn on ", '')
                command = 'on'
            if line.startswith("toggle "):
                line = line.replace("toggle ", '')
                command = 'toggle'
            if line.startswith("turn off "):
                line = line.replace("turn off ", '')
                command = 'off'

            values = line.split(' through ')
            instructions.append(
                    {'cmd': command,
                     'start': [int(x) for x in values[0].split(',')],
                     'end': [int(x) for x in values [1].split(',')]}
                )

        grid = [[0 for y in range(1000)] for x in range(1000)]

        for instruction in instructions:
            grid = do_instruction(instruction, grid)

        count_brightness(grid)


def do_instruction(instruction, grid):
    cmd = instruction['cmd']
    start_x = instruction['start'][0]
    start_y = instruction['start'][1]
    end_x = instruction['end'][0]
    end_y = instruction['end'][1]

    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            if cmd == 'on':
                grid[y][x] += 1
            elif cmd == 'off':
                if grid[y][x] > 0:
                    grid[y][x] -= 1
            elif cmd == 'toggle':
                grid[y][x] += 2
    return grid


def count_brightness(grid):
    brightness = 0
    for row in grid:
        for pos in row:
            brightness += pos
    print(brightness)


if __name__ == "__main__":
    main()

