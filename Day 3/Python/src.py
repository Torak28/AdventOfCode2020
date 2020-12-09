from functools import reduce

def load_data(file_name: str) -> list:
    lst = []
    with open(file_name) as f: 
        lines = f.readlines() 

    for elem in lines:
        lst.append(elem.strip())

    return lst

def applay_rule(pos: tuple, rule: tuple) -> tuple:
    pos = list(pos)
    for elem in rule:
        if elem[0] == 'right':
            pos[1] = (pos[1] + elem[1])
        elif elem[0] == 'down':
            pos[0] = (pos[0] + elem[1])
    return tuple(pos)


def one_star_alg(lst: list, rule: tuple) -> int:
    start = (0, 0)
    pos = start
    ans = []
    try:
        while True:
            pos = applay_rule(pos, rule)
            ans.append(lst[pos[0]][pos[1] % len(lst[pos[0]])])
    except IndexError:
        return ans.count('#')

def two_star_alg(lst: list, rules: list) -> int:
    start = (0, 0)
    ans = []
    for rule in rules:
        try:
            pos = start
            tmp = []
            while True:
                pos = applay_rule(pos, rule)
                tmp.append(lst[pos[0]][pos[1] % len(lst[pos[0]])])
        except IndexError:
            ans.append(tmp.count('#'))
    return reduce((lambda x, y: x * y), ans)

def main():
    data = load_data('../input.txt')
    dummy_data = ["..##.......",
                  "#...#...#..",
                  ".#....#..#.",
                  "..#.#...#.#",
                  ".#...##..#.",
                  "..#.##.....",
                  ".#.#.#....#",
                  ".#........#",
                  "#.##...#...",
                  "#...##....#",
                  ".#..#...#.#"]

    move_1 = ('right', 3)
    move_2 = ('down', 1)
    rule = (move_1, move_2)

    rules = [
        [('right', 1),('down', 1)],
        [('right', 3),('down', 1)],
        [('right', 5),('down', 1)],
        [('right', 7),('down', 1)],
        [('right', 1),('down', 2)],
    ]

    print(f'1st star: {one_star_alg(data, rule)}')
    print(f'2nd star: {two_star_alg(data, rules)}')

if __name__ == "__main__":
    main()