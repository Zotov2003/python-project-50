def format_plain(diff, parent=''):
    lines = []

    for key, value in diff.items():
        # Формируем текущий путь
        full_key = f"{parent}.{key}" if parent else key

        if value['status'] == 'added':
            # Если свойство добавлено, указываем его значение
            value_str = convert_value(value['value'])
            lines.append(f"Property '{full_key}' was added with value: {value_str}")

        elif value['status'] == 'removed':
            # Если свойство удалено
            lines.append(f"Property '{full_key}' was removed")

        elif value['status'] == 'changed':
            # Если свойство изменилось
            old_value_str = convert_value(value['old_value'])
            new_value_str = convert_value(value['new_value'])
            lines.append(f"Property '{full_key}' was updated. From {old_value_str} to {new_value_str}")

        elif value['status'] == 'nested':
            # Если свойство вложенное, рекурсивно обрабатываем его
            lines.extend(format_plain(value['children'], full_key))

        elif value['status'] == 'unchanged':
            # Если свойство не изменилось, пропускаем его
            continue

    return lines

def convert_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, (list, dict)):
        return '[complex value]'
    else:
        return value