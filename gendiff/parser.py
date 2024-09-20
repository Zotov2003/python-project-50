import argparse


def parser():
    parser = argparse.ArgumentParser(
            description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", type=str, help="")
    parser.add_argument("second_file", type=str, help="")
    parser.add_argument("-f", "--format", type=str,
                            help="set format of output",
                            default='stylish')

    args = parser.parse_args()
    return args
