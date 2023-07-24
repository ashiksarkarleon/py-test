import pytest


@pytest.mark.smoke
@pytest.mark.order1
def test_case3():
    print("Test case 3 Execution Successfully")

@pytest.mark.order2
@pytest.mark.smoke
def test_case4():
    print("Test case 4 Execution Successfully")