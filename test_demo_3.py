import pytest


@pytest.fixture
def common_function():
    name = input("Enter tour name -> ")
    return name


@pytest.mark.order(2)
def test_case5(common_function):
    print("Test case 5 Execution Successfully", common_function)


@pytest.mark.order(3)
def test_case6(common_function):
    print("Test case 6 Execution Successfully", common_function)


@pytest.mark.order(1)
def test_case7(common_function):
    print("Test case 7 Execution Successfully", common_function)
