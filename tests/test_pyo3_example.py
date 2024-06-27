import pyo3_example


def test_sum_as_string():
    assert pyo3_example.sum_as_string(1, 1) == "2"

def test_diff_as_string():
    assert pyo3_example.diff_as_string(3, 2) == "1"
