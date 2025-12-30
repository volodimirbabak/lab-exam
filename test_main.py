import pytest
from main import arithmetic_progression_element

def test_first():
    # Перевіряємо перший елемент (n=1). Має бути 5.
    assert arithmetic_progression_element(1) == 5

def test_step():
    # Перевіряємо другий елемент (n=2). 5 + 2 = 7.
    assert arithmetic_progression_element(2) == 7

def test_error():
    # Перевіряємо, чи програма видає помилку на мінусове число
    with pytest.raises(ValueError):
        arithmetic_progression_element(-10)