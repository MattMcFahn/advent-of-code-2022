"""AOC Day 1: https://adventofcode.com/2022/day/1"""

from collections import defaultdict


def read_input() -> dict[int, list]:
    """"""
    filepath = "inputs/day1.txt"
    elf_number = 0
    elves_calories = defaultdict(list)
    with open(filepath, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                elves_calories[elf_number].append(int(line.strip('\n')))
            else:
                elf_number += 1

    return elves_calories


def total_calories(calories: dict[int, list]) -> dict[int, int]:
    """Sum to get total cals"""
    total_calories = {i: sum(calorie_list) for (i, calorie_list) in calories.items()}
    return total_calories


if "__name__" == "__main__":
    elves_calories = read_input()
    total_cals = total_calories(calories=elves_calories)

    # Solution 1
    print(f"Solution 1: {max(total_cals.values())}")

    # Solution 2
    values = list(total_cals.values())
    values.sort(reverse=True)
    print(f"Solution 2: {sum(values[0:3])}")
