i = int(input())


def lucky_year(year):
    year_plus = year + 1
    if len(str(year_plus)) == len(set(str(year_plus))):
        print(year_plus)
    else:
        return lucky_year(year_plus)


lucky_year(i)