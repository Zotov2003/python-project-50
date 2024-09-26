from gendiff.file_loader import load_file
from gendiff.build_diff import build_diff
from gendiff.formatters import choosing_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generating the diff between two files with the specified format"""
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    diff = build_diff(data1, data2)
    return choosing_formatter(diff, format_name)
