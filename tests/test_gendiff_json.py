import pytest
from gendiff.gendiff import generate_diff

@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'

@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'

@pytest.fixture
def empty_path():
    return 'tests/fixtures/empty.json'

def test_generate_diff(file1_path, file2_path):
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''
    assert generate_diff(file1_path, file2_path).strip() == expected.strip()

def test_identical_files(file1_path):
    expected = """{
  common: {
    setting1: Value 1
    setting2: 200
    setting3: True
    setting6: {
      doge: {
        wow:
      }
      key: value
    }
  }
  group1: {
    baz: bas
    foo: bar
    nest: {
      key: value
    }
  }
  group2: {
    abc: 12345
    deep: {
      id: 45
    }
  }
}"""
    assert generate_diff(file1_path, file1_path).strip() == expected.strip()

def test_one_empty_file(empty_path, file1_path):
    expected = """{
  + common: {
    setting1: Value 1
    setting2: 200
    setting3: True
    setting6: {
      key: value
      doge: {
        wow:
      }
    }
  }
  + group1: {
    baz: bas
    foo: bar
    nest: {
      key: value
    }
  }
  + group2: {
    abc: 12345
    deep: {
      id: 45
    }
  }
}"""
    assert generate_diff(empty_path, file1_path).strip() == expected.strip()