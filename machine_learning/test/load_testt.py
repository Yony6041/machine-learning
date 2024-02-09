from machine_learning.homework.hw1.src.data.load_data import load_and_preprocess_data


def test_load_data():
    data = load_and_preprocess_data("data/raw/datos.csv")
    assert not data.empty, "La carga de datos falló, el DataFrame está vacío."
