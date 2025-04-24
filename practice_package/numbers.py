calculate_distance = lambda x1, x2: x2 - x1  # noqa: E731


calculate_segments = lambda a, b: a // b  # noqa: E731


calculate_digit_sum = lambda numik: sum(int(digit) for digit in str(abs(numik)))  # noqa: E731
    

def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)


def calculate_rect_area(x1, y1, x2, y2):
    perv = abs(x2 - x1)
    dvorf = abs(y2 - y1)
    return perv * dvorf