use std::fs::File;
use std::io::{BufRead, BufReader};

fn load_data() -> Vec<String>{
    let mut vec = Vec::new();

    let f = File::open("../input.txt").unwrap();
    let f = BufReader::new(f);

    for line in f.lines() {
        let line = line.expect("Unable to read line");
        vec.push(line);
    }

    return vec;
}

fn check_password_1_star(rule: &str, password: &str) -> bool{
    let tmp: Vec<&str> = rule.split(' ').collect();
    let number: &str = tmp[0];
    let letter: &str = tmp[1];
    let tmp: Vec<&str> = number.split('-').collect();
    let low: &str = tmp[0];
    let high: &str = tmp[1];

    let ans = password.matches(letter).count();
    if ans >= low.parse().unwrap() && ans <= high.parse().unwrap() {
        return true;
    }
    return false;
}

fn check_password_2_star(rule: &str, password: &str) -> bool{
    let tmp: Vec<&str> = rule.split(' ').collect();
    let number: &str = tmp[0];
    let letter: char = tmp[1].parse::<char>().unwrap();
    let tmp: Vec<&str> = number.split('-').collect();
    let present: usize = tmp[0].parse::<usize>().unwrap();
    let not_present: usize = tmp[1].parse::<usize>().unwrap();

    if (password.chars().nth(present).unwrap() == letter && password.chars().nth(not_present).unwrap() != letter) ||
       (password.chars().nth(present).unwrap() != letter && password.chars().nth(not_present).unwrap() == letter){
        return true;
    }
    return false;
}

fn one_star_alg(arr: &Vec<String>) -> i32{
    let mut ans: i32 = 0;

    for elem in arr {
        let tmp: Vec<&str> = elem.split(':').collect();
        let rule: &str = tmp[0];
        let password: &str = tmp[1];
        if check_password_1_star(rule, password){
            ans += 1;
        }
    }

    return ans;
}

fn two_star_alg(arr: &Vec<String>) -> i32{
    let mut ans: i32 = 0;

    for elem in arr {
        let tmp: Vec<&str> = elem.split(':').collect();
        let rule: &str = tmp[0];
        let password: &str = tmp[1];
        if check_password_2_star(rule, password){
            ans += 1;
        }
    }

    return ans;
}

fn main() {
    let data: Vec<String> = load_data();
    let _dummy_data: Vec<String> = vec!["1-3 a: abcde".to_string(), 
                                       "1-3 b: cdefg".to_string(), 
                                       "2-9 c: ccccccccc".to_string()];

    println!("1st star: {}", one_star_alg(&data));
    println!("2nd star: {}", two_star_alg(&data));
}
