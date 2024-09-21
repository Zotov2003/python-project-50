from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.file_loader import load_file
from gendiff.build_diff import build_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    diff = build_diff(data1, data2)
    return choosing_formatter(diff, format_name)


def choosing_formatter(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        format = format_plain(diff)
        return "\n".join(format)
    elif format_name == 'json':
        return format_json(diff)
