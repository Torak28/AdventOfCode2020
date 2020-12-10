def load_data(file_name: str) -> list:
    lst = []
    with open(file_name) as f: 
        lines = f.readlines() 

    for elem in lines:
        lst.append(elem.strip())

    return lst

def prep_passport(passport: str) -> dict:
    passport = passport.strip()
    passport = passport.split(' ')
    pre_dict = []
    for elem in passport:
        tmp = elem.split(':')
        pre_dict.append(tuple(tmp))
    
    ans = dict(pre_dict)

    return ans

def is_valid(passport: str, rule: dict) -> bool:
    passport = prep_passport(passport)
    ans = 0
    for key in list(rule.keys()):
        try:
            if passport[key] and rule[key] == 'required':
                ans += 1
            elif passport[key] and rule[key] == 'not_required':
                ans += 1
        except KeyError:
            if rule[key] == 'not_required':
                ans += 1
    if ans == len(rule):
        return True
    else:
        return False

def is_valid_2(passport: str, rule: dict) -> bool:
    passport = prep_passport(passport)
    ans = 0
    for key in list(rule.keys()):
        try:
            if passport[key] and rule[key] == 'required':
                if key == 'byr':
                    if int(passport[key]) >= 1920 and int(passport[key]) <= 2002:
                        ans += 1
                if key == 'iyr':
                    if int(passport[key]) >= 2010 and int(passport[key]) <= 2020:
                        ans += 1
                if key == 'eyr':
                    if int(passport[key]) >= 2020 and int(passport[key]) <= 2030:
                        ans += 1
                if key == 'hgt':
                    if passport[key][-2:] == 'cm':
                        if int(passport[key][:-2]) >= 150 and int(passport[key][:-2]) <= 193:
                            ans += 1
                    elif passport[key][-2:] == 'in':
                        if int(passport[key][:-2]) >= 59 and int(passport[key][:-2]) <= 76:
                            ans += 1
                if key == 'hcl':
                    if passport[key][0] == '#':
                        tmp = 0
                        for _ in passport[key][1:]:
                            if _ in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                                tmp += 1
                        if tmp == 6:
                            ans += 1
                if key == 'ecl':
                    if passport[key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        ans += 1
                if key == 'pid':
                    if len(passport[key]) == 9:
                        ans += 1
            elif passport[key] and rule[key] == 'not_required':
                ans += 1
        except KeyError:
            if rule[key] == 'not_required':
                ans += 1
    if ans == len(rule):
        return True
    else:
        return False

def one_star_alg(lst: list, rule: dict) -> int:
    ans = 0
    passport = ''
    passports = []
    for elem in lst:
        if elem != '':
            passport += elem
            passport += ' '
        else:
            passports.append(passport)
            passport = ''
    passports.append(passport)
    for passport in passports:
        ans += 1 if is_valid(passport, rule) else 0

    return ans

def two_star_alg(lst: list, rule: dict) -> int:
    ans = 0
    passport = ''
    passports = []
    for elem in lst:
        if elem != '':
            passport += elem
            passport += ' '
        else:
            passports.append(passport)
            passport = ''
    passports.append(passport)
    for passport in passports:
        ans += 1 if is_valid_2(passport, rule) else 0

    return ans

def main():
    data = load_data('../input.txt')
    dummy_data = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                  "byr:1937 iyr:2017 cid:147 hgt:183cm",
                  "",
                  "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                  "hcl:#cfa07d byr:1929",
                  "",
                  "hcl:#ae17e1 iyr:2013",
                  "eyr:2024",
                  "ecl:brn pid:760753108 byr:1931",
                  "hgt:179cm",
                  "",
                  "hcl:#cfa07d eyr:2025 pid:166559648",
                  "iyr:2011 ecl:brn hgt:59in"]

    rule = {
        "byr": "required",
        "iyr": "required",
        "eyr": "required",
        "hgt": "required",
        "hcl": "required",
        "ecl": "required",
        "pid": "required",
        "cid": "not_required"
    }

    print(f'1st star: {one_star_alg(data, rule)}')
    print(f'2nd star: {two_star_alg(data, rule)}')

if __name__ == "__main__":
    main()