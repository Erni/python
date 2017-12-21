def is_armstrong(number):
    if(number < 10):
        return True

    str_numer = str(number)
    pw = len(str_numer)

    sum = 0
    for c in str_numer:
        sum += int(c)**pw

    if sum == number:
        return True
    return False