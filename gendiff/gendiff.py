import json
import yaml

"""def generate_diff(filepath1, filepath2):


    with open(filepath1) as file1, open(filepath2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    keys = sorted(set(data1.keys()).union(data2.keys()))

    diff = []

    for key in keys:
        if key in data1 and key not in data2:
            diff.append(f"- {key}: {json.dumps(data1[key])}")
        elif key not in data1 and key in data2:
            diff.append(f"+ {key}: {json.dumps(data2[key])}")
        elif data1[key] != data2[key]:
            diff.append(f"- {key}: {json.dumps(data1[key])}")
            diff.append(f"+ {key}: {json.dumps(data2[key])}")
        else:
            diff.append(f"  {key}: {json.dumps(data1[key])}")

    diff_str = "{\n"
    for line in diff:
        diff_str += f"  {line}\n"
    diff_str += "}\n"

    return diff_str
"""

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    
def diff_build(data1, data2):
    diff = {}
    for key in set(data1.keys()).union(data2.keys()):
        if key not in data1:
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif data1[key] != data2[key]:
            diff[key] = {
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key],
            }
        else:
            diff[key] = {'type': 'unchanged', 'value': data1[key]}
    return diff

def format_stylish(diff, depth=0):
    indent = '    ' * depth  # Определяем отступ
    lines = []
    for key, value in diff.items():
        if value['type'] == 'added':
            lines.append(f"{indent}+ {key}: {value['value']}")
        elif value['type'] == 'removed':
            lines.append(f"{indent}- {key}: {value['value']}")
        elif value['type'] == 'changed':
            lines.append(f"{indent}- {key}: {value['old_value']}")
            lines.append(f"{indent}+ {key}: {value['new_value']}")
        else:  # 'unchanged'
            lines.append(f"{indent}  {key}: {value['value']}")
    return '\n'.join(lines)

def generate_diff(file1, file2):
    if file1.endswith('.json'):
        data1 = load_json(file1)
    elif file1.endswith('.yaml'):
        data1 = load_yaml(file1)
    else:
        raise ValueError("Unsupported file format for the first file.")

    if file2.endswith('.json'):
        data2 = load_json(file2)
    elif file2.endswith('.yaml'):
        data2 = load_yaml(file2)
    else:
        raise ValueError("Unsupported file format for the second file.")

    diff = diff_build(data1, data2)
    return format_stylish(diff)