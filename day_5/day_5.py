import argparse

def init_crates(input):
    indexes = {0:[]}
    crates = True
    for i in input:
        line = list(i)
        crate_count = 0
        if crates:
            for ind, pixel in enumerate(line):
                if pixel == '[':
                    crate_count = 1
                    index = ind + 1
                    if index in indexes.keys():
                        indexes[index].append(line[index])
                    else:
                        indexes[index] = [line[index]]
            if crate_count == 0:
                crates = False
    for i in indexes.keys():
        indexes[i].reverse()
    print(indexes)
    return indexes

def manage_stacks(input):
    stacks = init_crates(input)
    print_stack(stacks)
    index_list = list(stacks.keys())
    index_list.sort()
    print(index_list)
    for i in input:
        if i[0] == 'm':
            _, count , _, init , _, dest = i.split(' ')
            print('count:', count, 'from', init, 'dest', dest)
            for i in range(int(count)):
                crate =stacks[index_list[int(init)]].pop()
                stacks[index_list[int(dest)]].append(crate)
                print_stack(stacks)
    return(stacks)

def manage_stacks9001(input):
    print("9001")
    stacks = init_crates(input)
    print_stack(stacks)
    index_list = list(stacks.keys())
    index_list.sort()
    print(index_list)
    for i in input:
        if i[0] == 'm':
            _, count , _, init , _, dest = i.split(' ')
            print('count:', count, 'from', init, 'dest', dest)
            cratestack = []
            for i in range(int(count)):
                cratestack.append(stacks[index_list[int(init)]].pop())
            cratestack.reverse()
            stacks[index_list[int(dest)]].extend(cratestack)
            print_stack(stacks)
    return(stacks)

def print_stack(stack):
    index_list = list(stack.keys())
    index_list.sort()
    for i in index_list:
        print(i, stack[i])

def stack_top(stack):
    print("Stack top\n**********")
    stack_top = []
    index_list = list(stack.keys())
    index_list.sort()
    for i in range(1,len(index_list)):
        stack_top.append(stack[index_list[i]][-1])
    return stack_top

        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()

    stacks = manage_stacks(input)
    print(stack_top(stacks))

    stacks = manage_stacks9001(input)
    print(stack_top(stacks))
        
if __name__ == "__main__":
    main()