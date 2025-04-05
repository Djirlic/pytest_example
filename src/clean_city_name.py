def clean_city_name(city_name: str | None) -> str:
    if city_name is None:
        return "unknown"
    city_name = city_name.strip()
    if not city_name:
        return "unknown"
    return city_name.title()