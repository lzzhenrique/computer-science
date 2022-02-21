from is_odd import is_odd_func


def test_is_odd_when_number_is_odd_returns_true():
    'Para um numero impar a funcao deve retornar o valor True'
    assert is_odd_func(3) is True


def test_is_odd_when_number_is_even_returns_false():
    'Para um numero par a funcao deve retornar o valor False'
    assert is_odd_func(4) is False
