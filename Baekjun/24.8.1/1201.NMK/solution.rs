use std::collections::VecDeque;
use std::io::{self};

fn main() {
    // 표준 입력을 처리
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let parts: Vec<usize> = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, m, k) = (parts[0], parts[1], parts[2]);

    // 조건 검사
    if n > m * k || n - k < m - 1 {
        println!("-1");
        return;
    }

    // 초기 배열 생성
    let mut remaining_elements: VecDeque<usize> = ((k + 1)..=n).collect();
    let mut result: Vec<usize> = (1..=k).rev().collect();

    // 전체가 하나의 그룹일 경우 바로 출력
    if m - 1 == 0 {
        println!(
            "{}",
            result
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<String>>()
                .join(" ")
        );
        return;
    }

    // 그룹 분할 계산
    let (group_size, mut extra_elements) = ((n - k) / (m - 1), (n - k) % (m - 1));

    // 그룹별 요소 추가
    while !remaining_elements.is_empty() {
        let mut current_group = Vec::new();
        for _ in 0..group_size {
            if let Some(val) = remaining_elements.pop_front() {
                current_group.push(val);
            }
        }
        if extra_elements > 0 {
            if let Some(val) = remaining_elements.pop_front() {
                current_group.push(val);
            }
            extra_elements -= 1;
        }
        current_group.reverse();
        result.extend(current_group);
    }

    // 결과 출력
    println!(
        "{}",
        result
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
