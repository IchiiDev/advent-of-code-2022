##
## Advent of Code 2022, IchiiDev
## advent-of-code-2022
## File description:
## Day02: Rock Paper Scissors
##

VALUES="XYZ"

def retrieve_values(filename):
    file = open(filename, "r+")
    return file.read().split("\n")

def encounter_result(v1, v2):
    if (v1 == "A"):
        if (v2 == "X"):
            return 3
        if (v2 == "Y"):
            return 6
        if (v2 == "Z"):
            return 0
    if (v1 == "B"):
        if (v2 == "X"):
            return 0
        if (v2 == "Y"):
            return 3
        if (v2 == "Z"):
            return 6
    if (v1 == "C"):
        if (v2 == "X"):
            return 6
        if (v2 == "Y"):
            return 0
        if (v2 == "Z"):
            return 3

def calculate_points(values):
    results = []
    for fight in values:
        if fight == "": continue
        data = fight.split(" ")
        results.append(VALUES.index(data[1]) + 1 + encounter_result(data[0], data[1]))
    return results

def end_type(value):
    if (value == "X"):
        return 0
    if (value == "Y"):
        return 3
    if (value == "Z"):
        return 6

def expected_result_type(v1, v2):
    if (v1 == "A"):
        if (v2 == "X"):
            return 3
        if (v2 == "Y"):
            return 1
        if (v2 == "Z"):
            return 2
    if (v1 == "B"):
        if (v2 == "X"):
            return 1
        if (v2 == "Y"):
            return 2
        if (v2 == "Z"):
            return 3
    if (v1 == "C"):
        if (v2 == "X"):
            return 2
        if (v2 == "Y"):
            return 3
        if (v2 == "Z"):
            return 1


def get_best_encounters(values):
    results = []
    for fight in values:
        if (fight == ""): continue
        data = fight.split(" ")
        results.append(end_type(data[1]) + expected_result_type(data[0], data[1]))
    return results

if __name__ == "__main__":
    values = retrieve_values("day02/test-inputs.txt")
    # results = calculate_points(values)
    # print(f"Le résultat total est {sum(results)} points !")
    results = get_best_encounters(values)
    print(f"Le résultat total réel est {sum(results)} !")

