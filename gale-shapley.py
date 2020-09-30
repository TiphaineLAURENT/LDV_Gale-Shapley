from typing import List, Dict

PREFERENCES_COUNT = 4
PERSON_COUNT = 4

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


class Person(object):
    index: int = 0
    engaged_with = None
    preferences: List[int] = []
    to_propose: List[int] = []

    def __init__(self, preferences: List[int], index: int):
        self.preferences = preferences
        self.to_propose = preferences
        self.index = index

    def __repr__(self):
        return f"{self.index} engaged with {self.engaged_with.index if self.engaged_with else None}"

    def get_woman_index_not_proposed(self) -> int:
        return self.to_propose.pop(0)

    def engage(self, person) -> None:
        self.engaged_with = person
        person.engaged_with = self

    def disengage(self) -> None:
        self.engaged_with = None


def get_not_engaged(men: List[Person]) -> Person:
    for man in men:
        if man.engaged_with is None and man.proposed_to:
            return man

    return None


def get_person_by_index(index: int, persons: List[Person]) -> Person:
    for person in persons:
        if person.index == index:
            return person

    return None


def gale_shapley(menPreferences: dict, womenPreferences: dict) -> None:
    men = []
    for man, preferences in menPreferences.items():
        men.append(Person(preferences, man))

    women = []
    for woman, preferences in womenPreferences.items():
        women.append(Person(preferences, woman))

    # (man = get_not_engaged...) -> while man is not None:
    while (man := get_not_engaged(men)) is not None:
        woman_index = man.get_woman_index_not_proposed()
        woman = get_person_by_index(woman_index, women)

        if woman.engaged_with is None:
            woman.engage(man)
        else:
            man_engaged = woman.engaged_with
            if woman.preferences.index(man.index) < woman.preferences.index(man_engaged.index):
                man_engaged.disengage()
                woman.engage(man)

    print("Men", men)
    print("Women", women)


print("Men preferences", men)
print("Women preferences", women)
gale_shapley(men, women)
