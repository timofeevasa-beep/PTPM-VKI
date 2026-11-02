# hello
def validate_password(password: str) -> bool:

    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")

    if ' ' in password:
        raise ValueError("Пароль не должен содержать пробелы")

    if not (8 <= len(password) <= 20):
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_spec = False

    spec_chars = {'!', '@', '#', '$', '%', '^', '&', '*'}

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in spec_chars:
            has_spec = True

    return has_upper and has_lower and has_digit and has_spec
