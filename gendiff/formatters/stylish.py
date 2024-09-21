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
    items = []
    for k, v in value_dict.items():
        items.append(
            f"{indent_str(depth + 1)}{k}: {stylish_value(v, depth + 1)}")

    return '{\n' + '\n'.join(items) + '\n' + indent_str(depth) + '}'


def indent_str(depth, indent=4):
    return ' ' * (depth * indent)


def stylish(diff_item, depth):
    lines = []
    for key, node in diff_item.items():
        status = node['status']
        handler = {
            'added': stylish_added,
            'removed': stylish_removed,
            'unchanged': stylish_unchanged,
            'changed': stylish_changed,
            'nested': stylish_nested
        }.get(status)

        if handler:
            lines.append(handler(key, node, depth))

    return '\n'.join(lines)


def stylish_added(key, node, depth):
    return (
        f"{indent_str(depth - 1)}  + {key}: "
        f"{stylish_value(node['value'], depth)}"
    )


def stylish_removed(key, node, depth):
    return (
        f"{indent_str(depth - 1)}  - {key}: "
        f"{stylish_value(node['value'], depth)}"
    )


def stylish_unchanged(key, node, depth):
    return (
        f"{indent_str(depth)}{key}: "
        f"{stylish_value(node['value'], depth)}"
    )


def stylish_changed(key, node, depth):
    old_line = (
        f"{indent_str(depth - 1)}  - {key}: "
        f"{stylish_value(node['old_value'], depth)}"
    )
    new_line = (
        f"{indent_str(depth - 1)}  + {key}: "
        f"{stylish_value(node['new_value'], depth)}"
    )
    return old_line + '\n' + new_line


def stylish_nested(key, node, depth):
    nested_lines = stylish(node['children'], depth + 1)
    return (
        f"{indent_str(depth)}{key}: "
        f"{{\n{nested_lines}\n{indent_str(depth)}}}"
    )
