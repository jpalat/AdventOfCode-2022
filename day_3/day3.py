import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()

        
if __name__ == "__main__":
    main()