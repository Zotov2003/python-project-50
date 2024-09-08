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

def build_diff(dict1, dict2):
    differences = {}
    all_keys = dict1.keys() | dict2.keys()

    for key in sorted(all_keys):
        if key in dict1 and key not in dict2:
            differences[key] = {"status": "removed", "value": dict1[key]}
        elif key in dict2 and key not in dict1:
            differences[key] = {"status": "added", "value": dict2[key]}
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                # Если оба значения словари, рекурсивно ищем разницу
                children = build_diff(dict1[key], dict2[key])
                differences[key] = {"status": "nested", "children": children}
            elif dict1[key] != dict2[key]:
                differences[key] = {
                    "status": "changed",
                    "old_value": dict1[key],
                    "new_value": dict2[key]
                }
            else:
                differences[key] = {"status": "unchanged", "value": dict1[key]}

    return differences

def format_stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    formatted_lines = []

    for key, value in diff.items():
        if value["status"] == "added":
            formatted_lines.append(f"{indent}+ {key}: {value['value']}")
        elif value["status"] == "removed":
            formatted_lines.append(f"{indent}- {key}: {value['value']}")
        elif value["status"] == "changed":
            formatted_lines.append(f"{indent}- {key}: {value['old_value']}")
            formatted_lines.append(f"{indent}+ {key}: {value['new_value']}")
        elif value["status"] == "nested":
            formatted_lines.append(f"{indent}  {key}:")
            formatted_lines.append(format_stylish(value["children"], depth + 1))
        elif value["status"] == "unchanged":
            formatted_lines.append(f"{indent}  {key}: {value['value']}")

    return "\n".join(formatted_lines)

def generate_diff(filepath1, filepath2):
    with open(filepath1) as f1, open(filepath2) as f2:
        dict1 = load_file(filepath1)
        dict2 = load_file(filepath2)
        
    differences = build_diff(dict1, dict2)
    return format_stylish(differences)

def load_file(filepath):
    if filepath.endswith('.json'):
        with open(filepath) as f:
            return json.load(f)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        with open(filepath) as f:
            return yaml.safe_load(f)