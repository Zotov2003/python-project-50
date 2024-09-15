def format_stylish(diff, indent=4):
    return '{\n' + stylish(diff, 1) + '\n}'


def stylish_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def format_dict(value_dict, depth):
    items = [
        f"{indent_str(depth + 1)}{k}: {stylish_value(v, depth + 1)}"
        for k, v in value_dict.items()
    ]
    return '{\n' + '\n'.join(items) + '\n' + indent_str(depth) + '}'


def indent_str(depth, indent=4):
    return ' ' * (depth * indent)


def stylish(diff_item, depth):
    lines = []
    for key, node in diff_item.items():
        status = node['status']
        stylish_added(status, lines, depth, key, node)
        stylish_removed(status, lines, depth, key, node)
        stylish_unchanged(status, lines, depth, key, node)
        stylish_changed(status, lines, depth, key, node)
        stylish_nested(status, lines, depth, key, node)

    return '\n'.join(lines)


def stylish_added(status, lines, depth, key, node):
    if status == 'added':
        line = (
            f"{indent_str(depth - 1)}  + {key}: "
            f"{stylish_value(node['value'], depth)}"
        )
        lines.append(line)


def stylish_removed(status, lines, depth, key, node):
    if status == 'removed':
        line = (
            f"{indent_str(depth - 1)}  - {key}: "
            f"{stylish_value(node['value'], depth)}"
        )
        lines.append(line)


def stylish_unchanged(status, lines, depth, key, node):
    if status == 'unchanged':
        line = (
            f"{indent_str(depth)}{key}: "
            f"{stylish_value(node['value'], depth)}"
        )
        lines.append(line)


def stylish_changed(status, lines, depth, key, node):
    if status == 'changed':
        old_line = (
            f"{indent_str(depth - 1)}  - {key}: "
            f"{stylish_value(node['old_value'], depth)}"
        )
        new_line = (
            f"{indent_str(depth - 1)}  + {key}: "
            f"{stylish_value(node['new_value'], depth)}"
        )
        lines.append(old_line)
        lines.append(new_line)


def stylish_nested(status, lines, depth, key, node):
    if status == 'nested':
        nested_lines = stylish(node['children'], depth + 1)
        line = (
            f"{indent_str(depth)}{key}: "
            f"{{\n{nested_lines}\n{indent_str(depth)}}}"
        )
        lines.append(line)
