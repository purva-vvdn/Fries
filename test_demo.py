import pytest

def test_is_even():

    number = 4
    assert number % 2 == 0, f"{number} is not an even number."

# Test 2: Verify string contains a substring
def test_contains_substring():
    main_string = "Hello, World!"
    substring = "World"
    assert substring in main_string, f"'{substring}' is not in '{main_string}'."

# Test 3: Check if a list contains a specific element
def test_list_contains_element():
    elements = [1, 2, 3, 4, 5]
    element = 3
    assert element in elements, f"{element} is not in the list."

# Test 4: Validate addition operation
def test_addition():
    num1 = 10
    num2 = 20
    result = num1 + num2
    assert result == 30, f"Expected 30, but got {result}."

# Test 5: Test division by zero
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0