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
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()
    print('total: ', score_total(input)) 

        
if __name__ == "__main__":
    main()