import pytest
from calculator import Calculator #из файла calculator импортируй класс

calculator = Calculator()

@pytest.mark.skip(reason="починить тест позже") #указали параметр и причину #декоратор для пропуска теста
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

@pytest.mark.xfail
def test_sum_negative_nums(): #создали ранее в этом степе
    calculator = Calculator()
    res = calculator.sum(-6, -10)    
    assert res == -17

@pytest.mark.xfail(strict=True)
def test_sum_positive_and_negative_nums(): #создали ранее в этом степе
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums(): #проверка сложения десятичных дробей
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)  
    assert res == 9.9

def test_sum_zero_nums(): #проверка сложения целого числа и нуля
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

@pytest.mark.positive_test
def test_div_positive(): #проверка деления чисел
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

def test_avg_empty_list(): #проверка нахождения среднего для пустого списка
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

@pytest.mark.positive_test
def test_avg_positive(): #проверка нахождения среднего для списка
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5

@pytest.mark.parametrize( 'num1, num2, result', [(4, 5, 9)] )
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result

@pytest.mark.parametrize( 'num1, num2, result', 
[(4, 5, 9), (-6, -10, -16), (-6, 6, 0), (5.61, 4.29, 9.9),
(10, 0, 10)] )
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result
    
@pytest.mark.parametrize( 'nums, result', 
[ ([], 0), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5) ] )
def test_avg_empty_list(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result