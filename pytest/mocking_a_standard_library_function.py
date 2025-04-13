from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

@patch("color.sample")
def test_gen_hex_color(mock_sample, gen):
    mock_sample.return_value = 22, 235, 219
    assert next(gen) == "#16EBDB"
    mock_sample.assert_called_once()