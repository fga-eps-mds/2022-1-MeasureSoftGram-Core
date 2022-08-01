from src.core.agregation import agregation_operation
from src.core.weighting import weighting_operation
from tests.utils.aggregation_data import (
    WEIGHTS_1,
    WEIGHTS_2,
    VALUES_1,
    VALUES_2,
)
import pytest


def test_agregation_operation():
    weighted_value_1 = weighting_operation(VALUES_1, WEIGHTS_1)
    weighted_value_2 = weighting_operation(VALUES_2, WEIGHTS_2)
    assert pytest.approx(agregation_operation(weighted_value_1, WEIGHTS_1)) == 0.525711
    assert pytest.approx(agregation_operation(weighted_value_2, WEIGHTS_2)) == 0.813749
