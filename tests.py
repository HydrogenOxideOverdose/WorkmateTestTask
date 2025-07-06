import pytest
from parser_functions import *


def test_filter_lines_greater_than():
    args = type('Args', (), {'where': 'value>10'})
    lines = [{'value': 5}, {'value': 15}, {'value': 20}]
    result = filter_lines(args, lines)
    assert result == [{'value': 15}, {'value': 20}]

def test_filter_lines_less_than():
    args = type('Args', (), {'where': 'value<15'})
    lines = [{'value': 5}, {'value': 15}, {'value': 20}]
    result = filter_lines(args, lines)
    assert result == [{'value': 5}]

def test_filter_lines_wrong_separator():
    args = type('Args', (), {'where': 'value!10'})
    lines = [{'value': 5}, {'value': 15}, {'value': 20}]
    with pytest.raises(Exception) as exc_info:
        filter_lines(args, lines)
    assert str(exc_info.value) == 'Wrong where separator'

def test_filter_lines_wrong_parameter():
    args = type('Args', (), {'where': 'invalid>10'})
    lines = [{'value': 5}, {'value': 15}, {'value': 20}]
    with pytest.raises(Exception) as exc_info:
        filter_lines(args, lines)
    assert str(exc_info.value) == 'Wrong where parameter'

def test_filter_lines_no_filter():
    args = type('Args', (), {'where': None})
    lines = [{'value': 5}, {'value': 15}, {'value': 20}]
    result = filter_lines(args, lines)
    assert result == lines


def test_aggregate_min():
    args = type('Args', (), {'aggregate': 'value=min'})
    lines = [{'value': '5'}, {'value': '15'}, {'value': '10'}]
    result = aggregate_lines(args, lines)
    assert result == [{'value': 5.0}]

def test_aggregate_max():
    args = type('Args', (), {'aggregate': 'value=max'})
    lines = [{'value': '5'}, {'value': '15'}, {'value': '10'}]
    result = aggregate_lines(args, lines)
    assert result == [{'value': 15.0}]

def test_aggregate_avg():
    args = type('Args', (), {'aggregate': 'value=avg'})
    lines = [{'value': '5'}, {'value': '15'}, {'value': '10'}]
    result = aggregate_lines(args, lines)
    assert result == [{'value': 10.0}]

def test_wrong_aggregate_format():
    args = type('Args', (), {'aggregate': 'value_min'})
    lines = [{'value': '5'}]
    with pytest.raises(Exception) as exc_info:
        aggregate_lines(args, lines)
    assert "Wrong aggregate parameter, there is no '=' separator" in str(exc_info.value)

def test_wrong_aggregate_parameter():
    args = type('Args', (), {'aggregate': 'invalid=min'})
    lines = [{'value': '5'}]
    with pytest.raises(Exception) as exc_info:
        aggregate_lines(args, lines)
    assert "Wrong aggregate parameter, it's not in csv keys" in str(exc_info.value)

def test_unknown_aggregate_function():
    args = type('Args', (), {'aggregate': 'value=unknown'})
    lines = [{'value': '5'}]
    with pytest.raises(Exception) as exc_info:
        aggregate_lines(args, lines)
    assert "Wrong aggregate" in str(exc_info.value)

def test_no_aggregation():
    args = type('Args', (), {'aggregate': None})
    lines = [{'value': '5'}, {'value': '15'}]
    result = aggregate_lines(args, lines)
    assert result == lines

def test_sort_asc():
    args = type('Args', (), {'order_by': 'value=asc'})
    lines = [{'value': '15'}, {'value': '5'}, {'value': '10'}]
    result = sort_lines(args, lines)
    assert result == [{'value': '5'}, {'value': '10'}, {'value': '15'}]

def test_sort_desc():
    args = type('Args', (), {'order_by': 'value=desc'})
    lines = [{'value': '15'}, {'value': '5'}, {'value': '10'}]
    result = sort_lines(args, lines)
    assert result == [{'value': '15'}, {'value': '10'}, {'value': '5'}]

def test_wrong_order_by_format():
    args = type('Args', (), {'order_by': 'value_asc'})
    lines = [{'value': '5'}]
    with pytest.raises(Exception) as exc_info:
        sort_lines(args, lines)
    assert "Wrong order_by parameter, there is no '=' separator" in str(exc_info.value)

def test_wrong_order_by_parameter():
    args = type('Args', (), {'order_by': 'invalid=asc'})
    lines = [{'value': '5'}]
    with pytest.raises(Exception) as exc_info:
        sort_lines(args, lines)
    assert "Wrong order_by parameter, it's not in csv keys" in str(exc_info.value)

def test_unknown_sort_method():
    args = type('Args', (), {'order_by': 'value=unknown'})
    lines = [{'value': '5'}]
    with pytest.raises(Exception) as exc_info:
        sort_lines(args, lines)
    assert "Wrong sort method" in str(exc_info.value)

def test_sort_non_numeric():
    args = type('Args', (), {'order_by': 'value=asc'})
    lines = [{'value': 'apple'}, {'value': 'banana'}, {'value': 'cherry'}]
    with pytest.raises(Exception) as exc_info:
        sort_lines(args, lines)
    assert "Can't sort this type" in str(exc_info.value)

def test_no_sorting():
    args = type('Args', (), {'order_by': None})
    lines = [{'value': '15'}, {'value': '5'}]
    result = sort_lines(args, lines)
    assert result == lines