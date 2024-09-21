def format_plain(diff, parent=''):
    """Formatting the output of the diff with plain formatter"""
    lines = []
    for key, value in diff.items():
        full_key = f"{parent}.{key}" if parent else key
        lines.extend(handle_status(value, full_key))
    return lines


def handle_status(value, full_key):
    status_handlers = {
        'added': lambda: handle_added(full_key, value['value']),
        'removed': lambda: handle_removed(full_key),
        'changed': lambda:
        handle_changed(full_key, value['old_value'], value['new_value']),
        'nested': lambda: format_plain(value['children'], full_key),
        'unchanged': lambda: [],
    }
    return status_handlers[value['status']]()


def handle_added(full_key, value):
    """Helper function to process added keys"""
    return [
        f"Property '{full_key}' was added with value: {convert_value(value)}"]


def handle_removed(full_key):
    """Helper function to process removed keys"""
    return [f"Property '{full_key}' was removed"]


def handle_changed(full_key, old_value, new_value):
    """Helper function to process changed keys"""
    return ["Property '{}' was updated. From {} to {}".format(
        full_key, convert_value(old_value), convert_value(new_value)
    )]


def convert_value(value):
    """Formatting the output of the diff"""
    if value is None:
        return 'null'
    if isinstance(value, (list, dict)):
        return '[complex value]'
    return (
        str(f"{value}").lower() if isinstance(value, bool)
        or isinstance(value, int)
        else f"'{value}'"
    )
