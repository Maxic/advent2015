def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()
        content = [line.strip('\n').split('x') for line in content]

        sum_of_ribbon = 0

        for measurement in content:
            measurement = [int(i) for i in measurement]
            l = measurement[0]
            w = measurement[1]
            h = measurement[2]

            smallest_dimension = min(measurement)
            measurement.remove(smallest_dimension)
            second_smallest_dimension = min(measurement)
            ribbon_length = smallest_dimension * 2 + second_smallest_dimension * 2
            bow_length = l * w * h

            total_ribbon = ribbon_length + bow_length
            sum_of_ribbon += total_ribbon

        print(sum_of_ribbon)


if __name__ == "__main__":
    main()

