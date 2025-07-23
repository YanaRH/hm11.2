import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]

def test_filter_by_state_executed(operations):
    result = filter_by_state(operations, 'EXECUTED')
    assert len(result) == 2
    assert all(op['state'] == 'EXECUTED' for op in result)

def test_sort_by_date_desc(operations):
    result = sort_by_date(operations)
    assert result[0]['id'] == 1  # Latest date first

def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, reverse=False)
    assert result[0]['id'] == 3  # Earliest date first
