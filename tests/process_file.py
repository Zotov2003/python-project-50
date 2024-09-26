def process_file(file_path, formatter):
    # Проверка расширения файла
    if not file_path.endswith(('.json', '.yml')):
        raise Exception("Неподдерживаемое расширение файла.")

    # Проверка доступных форматеров
    available_formatters = ['stylish', 'plain', 'json']
    if formatter not in available_formatters:
        raise Exception("Выбранный форматер не существует.")
