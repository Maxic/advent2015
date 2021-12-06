def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip('\n').split(' -> ') for line in content]

        wire_dict = {}
        instructions = []

        for line in line_arr:
            inst = {}

            operation = line[0]
            wire = line[1]

            if operation.__contains__(" AND "):
                inst['op'] = 'AND'
                values = operation.split(" AND ")
                inst['dep1'] = values[0]
                inst['dep2'] = values[1]
            elif operation.__contains__(" OR "):
                inst['op'] = 'OR'
                values = operation.split(" OR ")
                inst['dep1'] = values[0]
                inst['dep2'] = values[1]
            elif operation.__contains__(" RSHIFT "):
                inst['op'] = 'RSHIFT'
                values = operation.split(" RSHIFT ")
                inst['dep1'] = values[0]
                inst['dep2'] = values[1]
            elif operation.__contains__(" LSHIFT "):
                inst['op'] = 'LSHIFT'
                values = operation.split(" LSHIFT ")
                inst['dep1'] = values[0]
                inst['dep2'] = values[1]
            elif operation.__contains__("NOT "):
                inst['op'] = 'NOT'
                values = operation.split("NOT ")
                inst['dep1'] = values[1]
            elif not operation.isdigit():
                inst['op'] = 'NONE'
                inst['dep1'] = operation
            else:
                wire_dict[wire] = int(operation)

            if inst:
                inst['wire'] = wire
                instructions.append(inst)

        wire_dict['b'] = 16076

        while instructions.__len__() > 0:
            new_instructions = []

            for inst in instructions:
                # If we have a binary operator
                if 'dep2' in inst:
                    # check if one of the values is already an int
                    if inst['dep1'] in wire_dict and inst['dep2'] in wire_dict:
                        value1 = wire_dict[inst['dep1']]
                        value2 = wire_dict[inst['dep2']]
                    elif inst['dep1'].isdigit() and inst['dep2'] in wire_dict:
                        value1 = int(inst['dep1'])
                        value2 = wire_dict[inst['dep2']]
                    elif inst['dep1'] in wire_dict and inst['dep2'].isdigit():
                        value1 = wire_dict[inst['dep1']]
                        value2 = int(inst['dep2'])
                    else:
                        new_instructions.append(inst)
                        continue
                    if inst['op'] == 'AND':
                        wire_dict[inst['wire']] = value1 & value2
                    if inst['op'] == 'OR':
                        wire_dict[inst['wire']] = value1 | value2
                    if inst['op'] == 'LSHIFT':
                        wire_dict[inst['wire']] = value1 << value2
                    if inst['op'] == 'RSHIFT':
                            wire_dict[inst['wire']] = value1 >> value2

                elif inst['op'] == 'NOT':
                    if inst['dep1'] in wire_dict:
                        wire_dict[inst['wire']] = wire_dict[inst['dep1']] ^ 0xffff
                    else:
                        new_instructions.append(inst)
                elif inst['op'] == 'NONE':
                    if inst['dep1'] in wire_dict:
                        wire_dict[inst['wire']] = wire_dict[inst['dep1']]
                    else:
                        new_instructions.append(inst)

            instructions = new_instructions

        print(wire_dict['a'])


if __name__ == "__main__":
    main()

