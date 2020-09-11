# A very elementary example of what it is to be an Abelian group.
def isAbelian(exp1, exp2):
    return exp2[::-1].lower().replace(" ", "") == exp1.lower().replace(" ", "")


if __name__ == '__main__':
    print(isAbelian("a + b", "b + a"))
    print(isAbelian("a + b", "c + a"))
