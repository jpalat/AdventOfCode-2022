import argparse



def assign_inventory(inventory):
    assignments = {1:0}
    id = 1
    for i in inventory:
        if i == '\n':
            id = id + 1
        else:
            if id in assignments.keys():
                total = assignments[id] + int(i)
                assignments[id] = total
            else:
                assignments[id] = int(i)
    return assignments

def find_max(assignments):
    max = (0,0)
    for id in assignments.keys():
        if max[1] < assignments[id]:
            max = (id, assignments[id])
    return max
        


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        inventory = my_file.readlines()

    assignments = assign_inventory(inventory)

    print(assignments)
    max = find_max(assignments)
    print(max)

if __name__ == "__main__":
    main()