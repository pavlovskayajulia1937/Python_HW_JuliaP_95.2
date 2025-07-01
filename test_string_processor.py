import pytest
from string_processor import StringProcessor

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello."),
        ("Hello", "Hello."),
        ("hello world", "Hello world."),
    ],
)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output

# Позитивные тесты (test_process_positive):

# Тест 1. Входная строка "hello" должна преобразоваться в "Hello.".
# Тест 2. Входная строка "Hello" уже начинается с заглавной буквы и заканчивается точкой, результат должен быть "Hello.".
# Тест 3. Входная строка "hello world" должна преобразоваться в "Hello world.".
# Негативные тесты (test_process_negative):

# Тест 1. Пустая строка должна преобразоваться в ".".
# Тест 2. Строка "   " (состоящая только из пробелов) должна преобразоваться в " . ".