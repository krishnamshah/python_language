import datetime
import pytest
from workingdaycalculator import WorkingDayCalculator

@pytest.fixture(autouse=True)
def test_is_workday():
    calculator = WorkingDayCalculator()

    # Test a weekday that is not a holiday
    date = datetime.datetime(2021, 1, 4)
    assert calculator.is_workday(date) == True

    # Test a weekend day
    date = datetime.datetime(2021, 1, 9)
    assert calculator.is_workday(date) == False

    # Test a holiday that has been set
    calculator.set_holidays([datetime.datetime(2021, 1, 4)])
    date = datetime.datetime(2021, 1, 4)
    assert calculator.is_workday(date) == False

    # Test a recurring holiday that has been set
    calculator.set_recurring_holidays([datetime.datetime(1, 1, 1)])
    date = datetime.datetime(2021, 1, 1)
    assert calculator.is_workday(date) == False


def test_add_workdays():
    calculator = WorkingDayCalculator()
    calculator.set_holidays([datetime.datetime(2004, 5, 27), datetime.datetime(2004, 5, 17)])

    # Test adding 0 workdays
    start_date = datetime.datetime(2021, 1, 4, 8, 0)
    num_workdays = 0
    expected_date = datetime.datetime(2021, 1, 4, 8, 0)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test adding 1 workday
    start_date = datetime.datetime(2021, 1, 4, 8, 0)
    num_workdays = 1
    expected_date = datetime.datetime(2021, 1, 5, 8, 0)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test adding 2 workdays
    start_date = datetime.datetime(2021, 1, 4, 8, 0)
    num_workdays = 2
    expected_date = datetime.datetime(2021, 1, 6, 8, 0)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test adding a fractional number of workdays
    start_date = datetime.datetime(2021, 1, 4, 9, 0)
    num_workdays = 1.5
    expected_date = datetime.datetime(2021, 1, 5, 13, 0)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test subtracting a fractional number of workdays
    start_date = datetime.datetime(2021, 1, 6, 8, 0)
    num_workdays = -1.5
    expected_date = datetime.datetime(2021, 1, 4, 12, 0)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date


    # Test adding 44.723656 workdays
    start_date = datetime.datetime(2004, 5, 24, 19, 3)
    num_workdays = 44.723656
    expected_date = datetime.datetime(2004, 7, 27, 13, 47)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test subtracting 6.7470217 workdays
    start_date = datetime.datetime(2004, 5, 24, 18, 3)
    num_workdays = -6.7470217
    expected_date = datetime.datetime(2004, 5, 13, 10, 1)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test adding 12.782709 workdays
    start_date = datetime.datetime(2004, 5, 24, 8, 3)
    num_workdays = 12.782709
    expected_date = datetime.datetime(2004, 6, 10, 14, 18)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date

    # Test adding 8.276628 workdays
    start_date = datetime.datetime(2004, 5, 24, 7, 3)
    num_workdays = 8.276628
    expected_date = datetime.datetime(2004, 6, 4, 10, 12)
    assert calculator.add_workdays(start_date, num_workdays) == expected_date
