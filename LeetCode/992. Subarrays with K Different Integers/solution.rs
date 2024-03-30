use std::collections::HashMap;

impl Solution {
    pub fn subarrays_with_k_distinct(a: Vec<i32>, k: i32) -> i32 {
        let mut counter: HashMap<i32, i32> = HashMap::new();
        let mut pre_cnt = 0;
        let mut l = 0;
        let mut res = 0;

        for r in 0..a.len() {
            *counter.entry(a[r]).or_insert(0) += 1;

            if counter.len() > k as usize {
                if let Some(val) = counter.get_mut(&a[l]) {
                    *val -= 1;
                    if *val == 0 {
                        counter.remove(&a[l]);
                    }
                }
                pre_cnt = 0;
                l += 1;
            }

            while let Some(&count) = counter.get(&a[l]) {
                if count > 1 {
                    if let Some(val) = counter.get_mut(&a[l]) {
                        *val -= 1;
                    }
                    pre_cnt += 1;
                    l += 1;
                } else {
                    break;
                }
            }

            if counter.len() == k as usize {
                res += pre_cnt + 1;
            }
        }

        res
    }
}
