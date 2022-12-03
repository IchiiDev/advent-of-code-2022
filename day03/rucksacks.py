##
## Advent of Code 2022, IchiiDev
## advent-of-code-2022
## File description:
## Day02/ Rucksacks
##

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def retrieve_values(filename):
    file = open(filename, "r+")
    return file.read().split("\n")

def parse_rucksacks(values: list[str]):
    results = []
    for sack in values:
        middle = len(sack) // 2
        for c in sack[:middle]:
            if c in sack[middle:]:
                results.append(priority.index(c) + 1)
                break
    return results

def parse_groups(values: list[str]):
    results = []
    index = 0
    for i in range(len(values) // 3):
        for c in values[index]:
            if c in values[index + 1] and c in values[index + 2]:
                results.append(priority.index(c) + 1)
                break
        index += 3
    return results

if __name__ == "__main__":
    values = retrieve_values("day03/rucksacks.txt")
    # results = parse_rucksacks(values)
    results = parse_groups(values)
    print(f"The total priority result is {sum(results)}")
