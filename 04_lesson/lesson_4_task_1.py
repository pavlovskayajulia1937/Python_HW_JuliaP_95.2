import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# ===== capitalize =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("étoile", "Étoile")  # Unicode
], ids=["ascii", "with space", "single word", "unicode"])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (None, None)  # Если метод обрабатывает None
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# ===== trim =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),  # Удаляет только начальные пробелы
    ("\t\nspace", "space"),  # Спецсимволы
    ("no_spaces", "no_spaces")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
def test_trim_negative():
    assert string_utils.trim("") == ""
    assert string_utils.trim(None) is None  # Если поддерживается

# ===== to_list =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c", ",", ["a", "b", "c"]),
    ("1-2-3", "-", ["1", "2", "3"]),
    ("a b c", " ", ["a", "b", "c"]),
    ("single", ",", ["single"])  # Нет разделителя
])
def test_to_list_positive(input_str, delimiter, expected):
    assert string_utils.to_list(input_str, delimiter) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, delimiter", [
    ("", ","),  # Пустая строка
    (None, ","),  # None
    ("a,b,c", None)  # None как разделитель
])
def test_to_list_negative(input_str, delimiter):
    if input_str is None or delimiter is None:
        assert string_utils.to_list(input_str, delimiter) == []
    else:
        assert string_utils.to_list(input_str, delimiter) == []

# ===== contains =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "o", False),
    ("", "a", False),
    ("   ", " ", True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
def test_contains_negative():
    with pytest.raises(TypeError):  # Ожидаем ошибку, если symbol — не строка
        string_utils.contains("SkyPro", 123)

# ===== delete_symbol =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Hello World", "l", "Heo Word"),
    ("NoMatch", "z", "NoMatch"),
    ("", "a", "")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
def test_delete_symbol_negative():
    assert string_utils.delete_symbol(None, "a") is None  # Если поддерживается
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"  # Пустой symbol

# ===== starts_with =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "s", False),  # Регистрозависимость
    (" hello", " ", True),
    ("", "", True)  # Спорный случай
])
def test_starts_with_positive(string, symbol, expected):
    assert string_utils.starts_with(string, symbol) == expected

# ===== ends_with =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "o", True),
    ("SkyPro", "O", False),
    ("end  ", " ", True),
    ("", "", True)
])
def test_ends_with_positive(string, symbol, expected):
    assert string_utils.end_with(string, symbol) == expected

# ===== is_empty =====
@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ("", True),
    (" ", False),
    ("\t\n", False),
    ("not empty", False)
])
def test_is_empty_positive(string, expected):
    assert string_utils.is_empty(string) == expected

@pytest.mark.negative
def test_is_empty_negative():
    assert string_utils.is_empty(None) is True  # Если None считается пустым