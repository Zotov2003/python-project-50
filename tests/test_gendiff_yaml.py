import pytest
from gendiff.gendiff import generate_diff

@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.yml'

@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.yml'

@pytest.fixture
def empty_path():
    return 'tests/fixtures/empty.yml'

def test_generate_diff(file1_path, file2_path):
    expected = '''{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}
'''
    assert generate_diff(file1_path, file2_path).strip() == expected.strip()

def test_identical_files(file1_path):
    expected = """{
    follow: false
    host: "hexlet.io"
    proxy: "123.234.53.22"
    timeout: 50
}"""
    assert generate_diff(file1_path, file1_path).strip() == expected.strip()

def test_one_empty_file(empty_path, file1_path):
    expected = """{
  + follow: false
  + host: "hexlet.io"
  + proxy: "123.234.53.22"
  + timeout: 50
}"""
    assert generate_diff(empty_path, file1_path).strip() == expected.strip()