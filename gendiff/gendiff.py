from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.file_loader import load_file


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        if key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children_diff = build_diff(data1[key], data2[key])
            diff[key] = {
                'status': 'nested',
                'children': children_diff
            }
        elif data1[key] != data2[key]:
            diff[key] = {'status': 'changed',
                         'old_value': data1[key],
                         'new_value': data2[key]}
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}

    return diff


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