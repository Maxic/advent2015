def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()
        content = [line.strip('\n').split('x') for line in content]

        sum_of_paper = 0

        for measurement in content:
            measurement = [int(i) for i in measurement]
            l = measurement[0]
            w = measurement[1]
            h = measurement[2]
            total_paper = 2 * l * w + 2 * w * h + 2 * h * l

            smallest_dimension = min(measurement)
            measurement.remove(smallest_dimension)
            second_smallest_dimension = min(measurement)
            total_paper = total_paper + smallest_dimension * second_smallest_dimension
            sum_of_paper += total_paper

        print(sum_of_paper)


if __name__ == "__main__":
    main()

