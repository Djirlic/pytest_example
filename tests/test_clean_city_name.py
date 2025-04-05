from src.clean_city_name import clean_city_name

def test_clean_city_name_with_none_returns_unknown():
    assert clean_city_name(None) == "unknown"