import json


def format_json(diff):
    return json.dumps(diff, indent=4)  # Форматируем с отступами для удобства чтения