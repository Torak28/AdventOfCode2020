def load_data(file_name: str) -> list:
    lst = []
    with open(file_name) as f: 
        lines = f.readlines() 

    for elem in lines:
        lst.append(elem[:-1])

    return lst

def check_password_1_star(rule: str, password: str) -> bool:
    number, letter = rule.split(' ')
    low, high = number.split('-')

    ans = password.count(letter)
    if ans >= int(low) and ans <= int(high):
        return True
    return False

def check_password_2_star(rule: str, password: str) -> bool:
    number, letter = rule.split(' ')
    present, not_present = number.split('-')

    if (password[int(present)] == letter and password[int(not_present)] != letter or
       password[int(present)] != letter and password[int(not_present)] == letter):
        return True
    return False

def one_star_alg(lst: list) -> int:
    ans = 0
    for elem in lst:
        rule, password = elem.split(':')
        ans += 1 if check_password_1_star(rule, password) else 0
    return ans

def two_star_alg(lst: list) -> int:
    ans = 0
    for elem in lst:
        rule, password = elem.split(':')
        ans += 1 if check_password_2_star(rule, password) else 0
    return ans

def main():
    data = load_data('../input.txt')
    dummy_data = ['1-3 a: abcde',
                  '1-3 b: cdefg',
                  '2-9 c: ccccccccc']

    print(f'1st star: {one_star_alg(data)}')
    print(f'2nd star: {two_star_alg(data)}')

if __name__ == "__main__":
    main()