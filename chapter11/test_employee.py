import pytest

from employee import Employee


@pytest.fixture
def create_employee():
    employee = Employee("Sam", "Brown", 5000)
    return employee


def test_give_default_rate(create_employee):
    assert create_employee.annual_salary == 5000


def test_give_custom_raise(create_employee):
    create_employee.give_raise(2000)
    assert create_employee.annual_salary == 2000
