import argparse

def check_compartments(bag):
    size = len(bag.rstrip())
    items = int(size/2)
    compartment1 = bag[0:items]
    compartment2 = bag[items:]
    return (compartment1, compartment2)

def compare_compartments(compartments):
    c1, c2 = compartments[0], compartments[1]
    # print('c1', c1, type(c1), 'c2', c2, type(c2))
    
    set1 = set(list(c1))
    set2 = set(list(c2))
    intersect = set1.intersection(set2)
    return list(intersect)[0]

def score(char):
    components = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return components.index(char)

def score_total(inventory):
    total = 0
    for i in inventory:
        total = total + score(compare_compartments(check_compartments(i)))
    return total

def find_badges(inventory):
    group = []

    for i in range(0, len(inventory), 3):
        # print(inventory[i].rstrip(), inventory[i+1].rstrip(), inventory[i+2].rstrip())
        sets = []
        for j in range(0,3):
            sets.append(set(list(inventory[i+j].rstrip())))
        badge = list(sets[0].intersection(sets[1]).intersection(sets[2]))[0]
        # print('badge:', badge, 'score', score(badge))
        group.append(badge)
    return group

def badge_total(inventory):
    total = 0
    for i in find_badges(inventory):
        total = total + score(i)
    return total
  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()
    print('total: ', score_total(input)) 

    print('part 2 total:', badge_total(input))

        
if __name__ == "__main__":
    main()