# Some cayley tables for set of integers modulo n.
# Late night hack.
def cayleyTableZ(n):
    tbl = [["+".ljust(len(str(n))+2, " ")], []] # Add 2 to "+ |" to accommodate "+" and " "

    # Addition
    for i in range(n):
        entry = []
        # Row index
        entry += [str(i).zfill(len(str(n))).ljust(len(str(n))+2)]

        for j in range(n):
            entry += [(i+j) % n]

            # Col header row, label it
            if i == 0:
                tbl[0].append((i+j) % n)

        tbl.append(entry)

    for i in range(len(tbl)):
        print(*tbl[i])


# A very elementary example of what it means to be an Abelian group.
def isAbelian(exp1, exp2):
    return exp2[::-1].lower().replace(" ", "") == exp1.lower().replace(" ", "")


if __name__ == '__main__':
    print(isAbelian("a + b", "b + a"))
    print(isAbelian("a + b", "c + a"))

    cayleyTableZ(5)
    cayleyTableZ(20)
    cayleyTableZ(100)
