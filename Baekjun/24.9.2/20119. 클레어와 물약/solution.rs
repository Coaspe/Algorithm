use std::collections::{HashSet, VecDeque};
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut recipes = Vec::with_capacity(m);
    for _ in 0..m {
        let recipe_line = input.next().unwrap().unwrap();
        let recipe: Vec<usize> = recipe_line
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        recipes.push(recipe);
    }

    let l: usize = input.next().unwrap().unwrap().parse().unwrap();
    let mut completed: HashSet<usize> = input
        .next()
        .unwrap()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut g: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
    let mut degree: Vec<i32> = vec![0; m];

    let mut queue: VecDeque<usize> = VecDeque::new();

    for i in 0..m {
        let recipe = &recipes[i];
        let k = recipe[0]; // 첫 번째 값 (재료 수)
        let r = recipe.last().unwrap(); // 마지막 값 (최종 결과)

        // k개의 재료 중 완료되지 않은 재료 처리
        for j in 1..=k {
            if !completed.contains(&recipe[j]) {
                g[recipe[j]].push(i); // 그래프에 추가
                degree[i] += 1; // 해당 레시피의 진입 차수 증가
            }
        }
    }

    for i in 0..m {
        if degree[i] == 0 {
            queue.push_back(i)
        }
    }

    while let Some(i) = queue.pop_front() {
        let recipe: &Vec<usize> = &recipes[i];
        let r = recipe.last().unwrap();
        if completed.contains(r) {
            continue;
        }

        completed.insert(*r);

        for &next in &g[*r] {
            degree[next] -= 1;
            if degree[next] == 0 {
                queue.push_back(next);
            }
        }
    }
    let mut completed = completed.into_iter().collect::<Vec<usize>>();
    completed.sort();
    println!("{}", completed.len());
    println!(
        "{}",
        completed
            .iter()
            .map(|&x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
