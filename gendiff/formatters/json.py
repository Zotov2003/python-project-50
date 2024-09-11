import json


def format_json(diff):
    # Форматируем с отступами для удобства чтения
    return json.dumps(diff, indent=4) 
