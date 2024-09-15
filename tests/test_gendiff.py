import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file1_path_y():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_path_y():
    return 'tests/fixtures/file2.yml'


def load_expected(file_name):
    with open(f'tests/fixtures/{file_name}', 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize(
    "file1, file2, formatting, expected_file",
    [
        ('empty.json', 'empty.json', 'plain', 'result_empty_plain.txt'), 
        ('empty.json', 'empty.json', 'stylish', 'result_empty_stylish.txt'), 
        ('file1.json', 'file1.json', 'plain', 'result_identical_files_plain.txt'), 
        ('file1.json', 'file1.json', 'stylish', 'result_identical_files_stylish.txt'),
        ('file1.json', 'file1.json', 'plain', 'result_identical_files_plain.txt'),
        ('file1.json', 'file2.json', 'plain', 'result_plain.txt'), 
        ('file1.json', 'file2.json', 'stylish', 'result_stylish.txt'),
    ]
)
def test_generate_diff(file1, file2, formatting, expected_file):
    file1_path = f'tests/fixtures/{file1}'
    file2_path = f'tests/fixtures/{file2}'
    expected = load_expected(expected_file)
    assert generate_diff(file1_path, file2_path, formatting) == expected