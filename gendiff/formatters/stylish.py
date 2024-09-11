def format_stylish(diff, indent=4, left = 2):
    def stylish_value(value, depth):
        if isinstance(value, dict):
            items = [f'{indent_str(depth + 1)}{k}: {stylish_value(v, depth + 1)}' for k, v in value.items()]
            return '{\n' + '\n'.join(items) + '\n' + indent_str(depth) + '}'
        else:
            return value

    def indent_str(depth):
        return ' ' * (depth * indent - left)

    def stylish(diff_item, depth):
        lines = []
        for key, node in diff_item.items():
            if node['status'] == 'added':
                lines.append(f'{indent_str(depth - 1)}  + {key}: {stylish_value(node["value"], depth)}')
            elif node['status'] == 'removed':
                lines.append(f'{indent_str(depth - 1)}  - {key}: {stylish_value(node["value"], depth)}')
            elif node['status'] == 'unchanged':
                lines.append(f'{indent_str(depth + 1)}{key}: {stylish_value(node["value"], depth)}')
            elif node['status'] == 'changed':
                lines.append(f'{indent_str(depth - 1)}  - {key}: {stylish_value(node["old_value"], depth)}')
                lines.append(f'{indent_str(depth - 1)}  + {key}: {stylish_value(node["new_value"], depth)}')
            elif node['status'] == 'nested':
                nested_lines = stylish(node['children'], depth + 1)
                lines.append(f'{indent_str(depth+2)}{key}: {{\n{nested_lines}\n{indent_str(depth)}}}')


        return '\n'.join(lines)

    return '{\n' + stylish(diff, 1) + '\n}'