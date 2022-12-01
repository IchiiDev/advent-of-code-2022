##
## Advent of Code 2022, IchiiDev
## advent-of-code-2022
## File description:
## Day 01: Calories
##

def retrieve_calories(filename):
    file = open(filename, "r+")
    return file.read()

def parse_elfs(buffer):
    items_per_elf = [0]
    elfs = 0
    has_values = False
    for i in buffer:
        if i == '\n':
            if has_values:
                has_values = False
                items_per_elf[elfs] += 1
            else:
                elfs += 1
                items_per_elf.append(0)
        else:
            has_values = True
    return items_per_elf

def calc_calories(buffer: str, elfs):
    calories = buffer.split()
    calc = []
    index = 0
    for elf in elfs:
        total = 0
        for i in range(elf):
            total += int(calories[index + i])
        calc.append(total)
        index += elf
    return calc



if __name__ == "__main__":
    calories = retrieve_calories("./day01/calories_input.txt")
    elfs = parse_elfs(calories)
    calc = calc_calories(calories, elfs)
    calc.sort(reverse=True)
    print(f"The result is {calc[0]} calories !")
