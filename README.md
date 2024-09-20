### Hexlet tests and linter status:
[![Actions Status](https://github.com/Zotov2003/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Zotov2003/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/e9217ef26ea5ccc208bd/maintainability)](https://codeclimate.com/github/Zotov2003/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/e9217ef26ea5ccc208bd/test_coverage)](https://codeclimate.com/github/Zotov2003/python-project-50/test_coverage)

Вычислитель отличий
Программа сравнивает два конфигурационных файла, форматов json и yaml, для уточнения подробностей введите gendiff -h

Пример использования gendiff file1.json file2.json
Результат строится на основе того, как изменилось содержимое во втором файле относительно первого. Ключи выводятся в алфавитном порядке.

Пример использования gendiff --format plain file1.json file2.json
Текст отражает ситуацию, словно мы объединили второй объект с первым

Пример использования gendiff --format json filepath1.json filepath2.json
Показывает вывод в структурированном формате json

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement" |