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



def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        if key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {'status': 'nested', 'children': build_diff(data1[key], data2[key])}
        elif data1[key] != data2[key]:
            diff[key] = {'status': 'changed', 'old_value': data1[key], 'new_value': data2[key]}
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}

    return diff

def format_stylish(diff, indent=2):
    def stylish_value(value, depth):
        if isinstance(value, dict):
            items = [f'{indent_str(depth + 1)}{k}: {stylish_value(v, depth + 1)}' for k, v in value.items()]
            return '{\n' + '\n'.join(items) + '\n' + indent_str(depth) + '}'
        else:
            return value

    def indent_str(depth):
        return ' ' * (depth * indent)

    def stylish(diff_item, depth):
        lines = []
        for key, node in diff_item.items():
            if node['status'] == 'added':
                lines.append(f'{indent_str(depth - 1)}  + {key}: {stylish_value(node["value"], depth)}')
            elif node['status'] == 'removed':
                lines.append(f'{indent_str(depth - 1)}  - {key}: {stylish_value(node["value"], depth)}')
            elif node['status'] == 'unchanged':
                lines.append(f'{indent_str(depth)}{key}: {stylish_value(node["value"], depth)}')
            elif node['status'] == 'changed':
                lines.append(f'{indent_str(depth - 1)}  - {key}: {stylish_value(node["old_value"], depth)}')
                lines.append(f'{indent_str(depth - 1)}  + {key}: {stylish_value(node["new_value"], depth)}')
            elif node['status'] == 'nested':
                nested_lines = stylish(node['children'], depth + 1)
                lines.append(f'{indent_str(depth)}{key}: {{\n{nested_lines}\n{indent_str(depth)}}}')

        return '\n'.join(lines)

    return '{\n' + stylish(diff, 1) + '\n}'


def generate_diff(file_path1, file_path2, format_name='stylish'):
    
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    

#plain

def format_plain(diff, parent=''):
    lines = []
    
    for key, value in diff.items():
        # Формируем текущий путь
        full_key = f"{parent}.{key}" if parent else key
        
        if isinstance(value, dict):
            # Если значение - словарь, рекурсивно обрабатываем его
            lines.extend(format_plain(value, full_key))
        else:
            # Обрабатываем статусы
            if isinstance(value, str) and value.startswith('+'):
                lines.append(f"Property '{full_key}' was added with value: {value[1:].strip()}")
            elif isinstance(value, str) and value.startswith('-'):
                lines.append(f"Property '{full_key}' was removed")
            elif isinstance(value, str) and value.startswith(' '):
                lines.append(f"Property '{full_key}' was unchanged")
            else:
                lines.append(f"Property '{full_key}' has an unexpected format")

    return lines