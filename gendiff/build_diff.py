def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        diff[key] = process_key(key, data1, data2)

    return diff


def process_key(key, data1, data2):
    if key not in data1:
        return {'status': 'added', 'value': data2[key]}
    elif key not in data2:
        return {'status': 'removed', 'value': data1[key]}
    elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return handle_nested_diff(key, data1[key], data2[key])
    elif data1[key] != data2[key]:
        return {'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]}
    else:
        return {'status': 'unchanged', 'value': data1[key]}


def handle_nested_diff(key, nested1, nested2):
    children_diff = build_diff(nested1, nested2)
    return {
        'status': 'nested',
        'children': children_diff
    }
