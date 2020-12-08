def load_data(file_name: str) -> list:
    lst = []
    with open(file_name) as f: 
        lines = f.readlines() 

    for elem in lines:
        lst.append(int(elem))

    return lst

def one_star_alg(lst: list) -> int:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if sum([lst[i], lst[j]]) == 2020:
                    return lst[i] * lst[j]

def two_star_alg(lst: list) -> int:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and sum([lst[i], lst[j]]) < 2020:
                for k in range(len(lst)):
                    if i != j != k:
                        if sum([lst[i], lst[j], lst[k]]) == 2020:
                            return lst[i] * lst[j] * lst[k]

def main():
    data = load_data('../input.txt')
    dummy_data = [1721, 979, 366, 299, 675, 1456]

    print(f'1st star: {one_star_alg(data)}')
    print(f'2nd star: {two_star_alg(data)}')

if __name__ == "__main__":
    main()