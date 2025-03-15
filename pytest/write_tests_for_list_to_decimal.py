import pytest

from numbers_to_dec import list_to_decimal

def test_num_is_bool():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, True, 3])

def test_num_is_not_int():
    with pytest.raises(TypeError):
        list_to_decimal([1.698, 2, '3'])

def test_num_is_out_of_range_0_9():
    with pytest.raises(ValueError):
        list_to_decimal([10])

@pytest.mark.parametrize("data, expected", [
    ([0,0,5,8], 58), ([4,3,1,2], 4312), ([6,0,9,0,0,7], 609007), ([8], 8)
])
def test_numbers_0_9(data, expected):
    assert list_to_decimal(data) == expected