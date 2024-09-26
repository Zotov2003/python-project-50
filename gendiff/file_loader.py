import json
import yaml
import os


def parse_content(file_path, content):
    ext = get_extension(file_path)
    if ext == '.json':
        return json.loads(content)
    elif ext in ['.yml', '.yaml']:
        return yaml.safe_load(content)
    else:
        raise ValueError("Unsupported file format")


def load_file(file_path):
    """Load and parse a file based on its extension"""
    # _, ext = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        content = file.read()
        return parse_content(file_path, content)


def get_extension(file_path):
    """Extension Processing"""
    _, ext = os.path.splitext(file_path)
    return ext
