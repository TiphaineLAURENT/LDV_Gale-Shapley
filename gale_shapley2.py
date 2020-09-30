def find_stable_matching(menPreferences: dict, womenPreferences: dict) -> list:
    """
    Takes two dict[int, list[int]] and find perfect mariage using gale-shapley algorithm
    https://en.wikipedia.org/wiki/Gale–Shapley_algorithm
    """
    n = len(menPreferences)
    unmarriedMen = list(range(n))

    manSpouse = [None] * n # [None, None, None, None, None, None, ... n]
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    while unmarriedMen:
        he = unmarriedMen[0]

        hisPreferences = menPreferences[he]
        she = hisPreferences[nextManChoice[he]]

        herPreferences = womenPreferences[she]
        currentHusband = womanSpouse[she]

        if currentHusband is None:
            womanSpouse[she] = he
            manSpouse[he] = she

            nextManChoice[he] = nextManChoice[he] + 1

            unmarriedMen.pop(0)
        else:
            currentIndex = herPreferences.index(currentHusband)
            hisIndex = herPreferences.index(he)

            if currentIndex > hisIndex:
                womanSpouse[she] = he
                manSpouse[he] = she

                nextManChoice[he] = nextManChoice[he] + 1

                unmarriedMen[0] = currentHusband
            else:
                nextManChoice[he] = nextManChoice[he] + 1

    return manSpouse

men = {
    0: [2, 3, 1, 0],  # always 4 preferences
    1: [2, 0, 1, 3],
    2: [3, 0, 1, 2],
    3: [3, 2, 1, 0]
}  # always 4 men

women = {
    0: [3, 0, 2, 1],  # always 4 preferences
    1: [1, 2, 0, 3],
    2: [1, 2, 3, 0],
    3: [3, 1, 0, 2]
}  # always 4 women

print("Men preferences", men)
print("Women preferences", women)

print(find_stable_matching(men, women))
