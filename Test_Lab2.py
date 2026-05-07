import ex2 as lab2

def test_calc_average_temperature():
    result = lab2.calc_average_temperature([10, 20, 30])
    assert result == 20.0


def test_calc_min_max_temperature():
    result = lab2.calc_min_max_temperature([10, 20, 30, 5])
    assert result == [5, 30]


def test_calc_median_temperature_odd():
    result = lab2.calc_median_temperature([10, 30, 20])
    assert result == 20


def test_calc_median_temperature_even():
    result = lab2.calc_median_temperature([10, 20, 30, 40])
    assert result == 25.0