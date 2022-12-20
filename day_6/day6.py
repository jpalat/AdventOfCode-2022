import argparse

def sop_finder(signal):
    for n in range(3, len(signal)):
        buffer = set()
        for m in range(0,4):
            buffer.add(signal[n-m])
        if len(buffer) >3:
            # print(buffer)
            return n+1
    return -1

def som_finder(signal):
    for n in range(3, len(signal)):
        buffer = set()
        for m in range(0,14):
            buffer.add(signal[n-m])
        if len(buffer) >13:
            # print(buffer)
            return n+1
    return -1



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()

    for i in input:
        print('sop',sop_finder(i))
        print('som',som_finder(i))

        
if __name__ == "__main__":
    main()