import argparse
import re


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace.password:
        exit('Укажите пароль')
    print(get_password_strength(namespace.password))


def create_parser():
    parser = argparse.ArgumentParser(prefix_chars='-+/')
    parser.add_argument('password', nargs='?', default=False, help='Password')
    return parser


def get_password_strength(password):
    requierements = [
        is_different_case(password),
        is_at_least_one_digit(password),
        is_special_symbols(password),
        is_length_more_n(password)
    ]
    return calculate_strength_password(requierements)


def calculate_strength_password(requierements):
    fulfilled_requirements = [req for req in requierements if req]
    return round(len(fulfilled_requirements) / len(requierements) * 10)


def is_different_case(password):
    if re.search(r'[a-zA-Z]', password):
        is_lower = re.search(r'[a-z]', password) is not None
        is_upper = re.search(r'[A-Z]', password) is not None
        return is_lower and is_upper


def is_at_least_one_digit(password):
    return re.search(r'[\d]', password) is not None


def is_special_symbols(password):
    return re.search(r'\W', password) is not None


def is_length_more_n(password, n=8):
    return len(password) > n


if __name__ == '__main__':
    main()
