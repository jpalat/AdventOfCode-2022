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
        
def find_top3(assignments):
    values = list(assignments.values())
    values.sort(reverse=True)
    # print("vals", values)

    sum = 0
    for i in range(0,3):
        sum = values[i] + sum
    return sum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        inventory = my_file.readlines()

    assignments = assign_inventory(inventory)

    max = find_max(assignments)
    print('part 1:',max)
    top3 = find_top3(assignments)
    print('part 2:',top3)

if __name__ == "__main__":
    main()