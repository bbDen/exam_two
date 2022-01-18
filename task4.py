def calculate_nums(*args):
    summ = 0
    for i in args:
        if isinstance(i, (int, float)):
            summ = summ + i
    return summ
