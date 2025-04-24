extract_file_name = \
    lambda full_file_name: full_file_name.split('/')[-1].split('.')[0]  # noqa: E731


def encrypt_sentence(str):
    start = str[::2]
    end = str[1::2]
    return end + start[::-1]


def check_brackets(expression):
    openCount = 0
    closeCount = 0
    pos = 0
    for i in range(0, len(expression)):
        if expression[i] != ' ':
            pos += 1
        if expression[i] == '(':
            openCount += 1
        elif expression[i] == ')':
            closeCount += 1
        if closeCount > openCount:
            return pos
    if openCount > closeCount:
        return -1
    return 0


def reverse_domain(domain):
    parts = domain.split('.')
    reversed_parts = parts[::-1]
    return '.'.join(reversed_parts)


def count_vowel_groups():
    pass
