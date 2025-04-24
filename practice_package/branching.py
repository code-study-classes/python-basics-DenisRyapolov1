def is_weekend(day):
    return day == 6 or day == 7


def get_discount(amount):
    return (
        amount / 10 if amount >= 5000 else
        amount / 20 if amount >= 1000 else
        0
    )


def describe_number(n):
    chet = 'четное' if n % 2 == 0 else 'нечетное'
    znaki = 'однозначное' if len(str(n)) == 1 else \
        'двузначное' if len(str(n)) == 2 else \
        'трехзначное'
    return f"{chet} {znaki} число"


def convert_to_meters(unitNumber, lengthInUnits):
    match unitNumber:
        case 1:
            return lengthInUnits / 10
        case 2:
            return lengthInUnits * 1000
        case 3:
            return lengthInUnits
        case 4:
            return lengthInUnits / 1000
        case 5:
            return lengthInUnits / 100
        

def describe_age(age):
    pass