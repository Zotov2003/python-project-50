import pytest
import hexlet_code.gendiff as a

@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'

@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'

def test_generate_diff(file1_path, file2_path):
    expected = """{
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert a.generate_diff(file1_path, file2_path).strip() == expected.strip()

def test_identical_files(file1_path):
    # Тест на идентичные файлы
    assert a.generate_diff(file1_path, file1_path).strip() == "{}"

def test_empty_and_non_empty_files():
    # Пример для пустого файла и файла с данными
    empty_file_path = 'tests/fixtures/empty.json'
    filled_file_path = 'tests/fixtures/file1.json'
    
    expected = """{
  - timeout: 50
  - proxy: 123.234.53.22
  - follow: false
  - host: hexlet.io
}"""
    
    assert a.generate_diff(empty_file_path, filled_file_path).strip() == expected.strip()