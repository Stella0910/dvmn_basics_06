def has_digit(password):
    return any(character.isdigit() for character in password)


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


def has_symbols(password):
    return any(not character.isdigit() and not character.isalpha()
               for character in password)


def main():
    password_checks = [is_very_long, has_digit,
                       has_upper_letters,
                       has_lower_letters,
                       has_symbols,
                       ]
    score = 0
    password_option = input("Введите пароль: ")
    for check in password_checks:
        if check(password_option):
            score = score + 2
    print(f"Рейтинг пароля: {score}")


if __name__ == '__main__':
    main()
