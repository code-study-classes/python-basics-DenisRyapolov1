check_between_numbers = lambda A, B, C: A > B > C or A < B < C  # noqa: E731

check_odd_three = lambda number: 100 <= number <= 999 and not number // 2  # noqa: E731
    

check_unique_digits = lambda number: len(set(str(number))) == 3 and 100 \
      <= number <= 999  # noqa: E731
   

def check_palindrome_number(number):
    return str(number)[::1] == str(number)


def check_ascending_digits(number):
    pass