def square_odds(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0: 
            result.append(num ** 2) 
    return result


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    validno = []
    for email in emails:
        if (email.count('@') == 1 and
            len(email) >= 5 and
            not email.startswith('@') and
            not email.endswith('@')):
            validno.append(email)
    return validno


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_common_prefix(strings):
    pass