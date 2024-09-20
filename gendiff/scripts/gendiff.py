from gendiff.parser import parser
from gendiff.gendiff import generate_diff


def main():
    args = parser()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
