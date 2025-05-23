import pytest
from my_awesome_lib.math_tools import mean_weighted, std_dev

def test_mean_weighted_basic():
    assert mean_weighted([1, 2, 3], [1, 1, 1]) == 2.0

def test_mean_weighted_zero_weights():
    with pytest.raises(ValueError):
        mean_weighted([1, 2], [0, 0])

def test_std_dev_single_value():
    with pytest.raises(ZeroDivisionError):
        std_dev([42])

def test_std_dev_population_vs_sample():
    sample = [2, 4, 4, 4, 5, 5, 7, 9]
    # z Wikipedii: odchylenie populacyjne = 2, sample (ddof=1) ≈ 2.138
    assert std_dev(sample, ddof=0) == 2.0
    assert abs(std_dev(sample, ddof=1) - 2.1380899) < 1e-6
