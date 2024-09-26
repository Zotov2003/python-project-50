def format_stylish(diff, indent=4):
    """Formatting the output of the diff with stylish formatter"""
    return '{\n' + get_style_stylish(diff, 1) + '\n}'


def stylish_value(value, depth):
    """Formatting the output of the diff"""
    if isinstance(value, dict):
        return formating_dict(value, depth)
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def formating_dict(value_dict, depth):
    items = []
    for k, v in value_dict.items():
        items.append(
            f"{insert_indent_str(depth + 1)}{k}: {stylish_value(v, depth + 1)}")

    return '{\n' + '\n'.join(items) + '\n' + insert_indent_str(depth) + '}'


def insert_indent_str(depth, indent=4):
    return ' ' * (depth * indent)


def get_style_stylish(diff_item, depth):
    lines = []
    for key, node in diff_item.items():
        status = node['status']
        handler = {
            'added': get_stylish_added,
            'removed': get_stylish_removed,
            'unchanged': get_stylish_unchanged,
            'changed': get_stylish_changed,
            'nested': get_stylish_nested
        }.get(status)

        if handler:
            lines.append(handler(key, node, depth))

    return '\n'.join(lines)


def get_stylish_added(key, node, depth):
    """Helper function to process added keys"""
    return (
        f"{insert_indent_str(depth - 1)}  + {key}: "
        f"{stylish_value(node['value'], depth)}"
    )


def get_stylish_removed(key, node, depth):
    """Helper function to process removed keys"""
    return (
        f"{insert_indent_str(depth - 1)}  - {key}: "
        f"{stylish_value(node['value'], depth)}"
    )


def get_stylish_unchanged(key, node, depth):
    """Helper function to process unchanged keys"""
    return (
        f"{insert_indent_str(depth)}{key}: "
        f"{stylish_value(node['value'], depth)}"
    )


def get_stylish_changed(key, node, depth):
    """Helper function to process changed keys"""
    old_line = (
        f"{insert_indent_str(depth - 1)}  - {key}: "
        f"{stylish_value(node['old_value'], depth)}"
    )
    new_line = (
        f"{insert_indent_str(depth - 1)}  + {key}: "
        f"{stylish_value(node['new_value'], depth)}"
    )
    return old_line + '\n' + new_line


def get_stylish_nested(key, node, depth):
    """Helper function to process nested nodes (children)"""
    nested_lines = get_style_stylish(node['children'], depth + 1)
    return (
        f"{insert_indent_str(depth)}{key}: "
        f"{{\n{nested_lines}\n{insert_indent_str(depth)}}}"
    )
