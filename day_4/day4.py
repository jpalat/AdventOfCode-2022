import argparse

def parse(line):
    return line.rstrip().split(',')
    
def ranger(elf):
    begin,end = elf.split('-')
    if begin == end:
        return {int(begin)}
    return set(range(int(begin), int(end)+1))

def range_check(line):
    elf1, elf2 = parse(line)
    r1 = ranger(elf1)
    r2 = ranger(elf2)
    if len(r1) == len(r1.union(r2)) or len(r2) == len(r1.union(r2)):
        return True
    return False

def range_check2(line):
    elf1, elf2 = parse(line)
    r1 = ranger(elf1)
    r2 = ranger(elf2)
    if len(r1.intersection(r2)) > 0:
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()
    
    total_overlaps = 0
    for i in input:
        if range_check(i):
            total_overlaps = total_overlaps + 1
    print('overlaps', total_overlaps)

    total_overlaps = 0
    for i in input:
        if range_check2(i):
            total_overlaps = total_overlaps + 1
    print('overlaps', total_overlaps)

        
if __name__ == "__main__":
    main()