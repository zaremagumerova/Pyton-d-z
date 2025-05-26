import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   Hello world   ", "Hello world   "),
    (" Hello!", "Hello!"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected_exception", [
     ("Gaz", "G", True),
      ("Gaz", "s", False),
      ("Собака", "С", True),
      ("Кот", "д", False),
      ("Red1", "R", True),
      ("Red2", "Y", False),
      ("Red1", "1", True),
      ("Red1", "e", True)
  
])
def test_contains_positive(input_str, symbol, expected_exception):
    assert string_utils.contains(input_str,symbol) == expected_exception


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected_exception", [
     ("Gaz", "G", "az"),
      ("Gaz1", "az", "G1"),
      ("1234", "4", "123"),
      ("Котёнок", "ёнок", "Кот"),
      ("Спасибо!", "!", "Спасибо"),
      ("1+0=1", "+0", "1=1"),
  
])
def test_delete_symbol_positive(input_str, symbol, expected_exception):
    assert string_utils.delete_symbol(input_str,symbol) == expected_exception



@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Zara", "Zara"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
    ("...", "..."),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize("input_str, symbol, expected_expection", [
    ("123", "c", False),
    ([], "c", False),
    ((), "a", False),
    ("", "Z", False)
])
def test_contains_negative(input_str, symbol, expected_expection):
    assert string_utils.contains(input_str,symbol) == expected_exception

@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize("input_str, symbol, expected_expection", [
    ("ZaraVal", "", "ZaraVal"),
    ("", "v", ""),
    ("cat", "s", "cat")
    ])
def test_delete_symbol_negative(input_str, symbol, expected_expection):
    assert string_utils.delete_symbol(input_str,symbol) == expected_exception