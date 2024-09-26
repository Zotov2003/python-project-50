def format_plain(diff, parent=""):
    lines = []

    for key, value in diff.items():
        full_key = f"{parent}.{key}" if parent else key

        if value['status'] == 'added':
            lines.append(
                f"Property '{full_key}' was added with value: "
                f"{format_value(value['value'])}")
        elif value['status'] == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif value['status'] == 'changed':
            lines.append(
                f"Property '{full_key}' was updated. "
                f"From {format_value(value['old_value'])} "
                f"to {format_value(value['new_value'])}")
        elif value['status'] == 'nested':
            lines.append(format_plain(value['children'], full_key))

    return "\n".join(lines)


def format_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, list) or isinstance(value, dict):
        return "[complex value]"
    elif value is None:
        return "null"
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
