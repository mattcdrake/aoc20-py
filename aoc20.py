import day_1
import day_2


def solve_puzzles() -> None:
    print("Solving...")
    print("----------")
    print(f'Day 1, Puzzle 1: {day_1.p1("./input/day1.txt")}')
    print(f'Day 1, Puzzle 2: {day_1.p2("./input/day1.txt")}')
    print(f'Day 2, Puzzle 1: {day_2.p1("./input/day2.txt")}')
    print(f'Day 2, Puzzle 2: {day_2.p2("./input/day2.txt")}')


if __name__ == "__main__":
    solve_puzzles()

