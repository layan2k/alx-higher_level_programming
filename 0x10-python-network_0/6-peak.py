#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    md = int(length / 2)
    ls = list_of_integers

    if md - 1 < 0 and md + 1 >= length:
        return ls[md]
    elif md - 1 < 0:
        return ls[md] if ls[md] > ls[md + 1] else ls[md + 1]
    elif md + 1 >= length:
        return ls[md] if ls[md] > ls[md - 1] else ls[md - 1]

    if ls[md - 1] < ls[md] > ls[md + 1]:
        return ls[md]

    if ls[md + 1] > ls[md - 1]:
        return find_peak(ls[md:])
    return find_peak(ls[:md])
