from src.clean_city_name import clean_city_name

def test_clean_city_name_with_none_returns_unknown():
    assert clean_city_name(None) == "unknown"

def test_clean_city_name_with_empty_string_returns_unknown():
    assert clean_city_name("") == "unknown"

def test_clean_city_name_with_city_returns_city_in_title_case():
    assert clean_city_name("united states") == "United States"
  
def test_clean_city_name_with_whitespace_returns_unknown():
    assert clean_city_name("   ") == "unknown"