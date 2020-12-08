use std::fs::File;
use std::io::{BufRead, BufReader};

fn load_data() -> Vec<i32>{
    let mut vec = Vec::new();

    let f = File::open("../input.txt").unwrap();
    let f = BufReader::new(f);

    for line in f.lines() {
        let line = line.expect("Unable to read line");
        vec.push(line.parse::<i32>().unwrap());
    }

    return vec;
}

fn one_star_alg(arr: &[i32]) -> i32{
    let mut ans: i32 = 0;

    'main_loop: for i in 0..arr.len() {
        for j in 0..arr.len() {
            if i != j{
                if arr[i] + arr[j] == 2020 {
                    ans = arr[i] * arr[j];
                    break 'main_loop
                }
            }
        }
    }
    return ans;
}

fn two_star_alg(arr: &[i32]) -> i32{
    let mut ans: i32 = 0;

    'main_loop: for i in 0..arr.len() {
        for j in 0..arr.len() {
            for k in 0..arr.len() {
                if i != j && i != k && k != j{
                    if arr[i] + arr[j] + arr[k] == 2020 {
                        ans = arr[i] * arr[j] * arr[k];
                        break 'main_loop
                    }
                }
            }
        }
    }
    return ans;
}

fn main() {
    let data: Vec<i32> = load_data();
    let _dummy_data: Vec<i32> = vec![1721, 979, 366, 299, 675, 1456];

    println!("1st star: {}", one_star_alg(&data));
    println!("2nd star: {}", two_star_alg(&data));
}
