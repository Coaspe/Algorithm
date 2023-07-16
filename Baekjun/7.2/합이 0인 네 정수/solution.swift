import Foundation

func readInt() -> Int {
    return Int(readLine()!)!
}

if let n = readInt() {
    var arr: [[Int]] = []
    for _ in 0..<n {
        let input = readLine()!.split(separator: " ").map { Int($0)! }
        arr.append(input)
    }
    
    var ab: [Int] = []
    var cd: [Int] = []
    
    for i in 0..<n {
        for j in 0..<n {
            ab.append(arr[i][0] + arr[j][1])
            cd.append(arr[i][2] + arr[j][3])
        }
    }
    
    ab.sort()
    cd.sort { $0 > $1 }
    
    var result = 0
    var i = 0
    var j = 0
    
    while i < ab.count && j < cd.count {
        if ab[i] + cd[j] == 0 {
            var count_ab = 1
            var count_cd = 1
            i += 1
            j += 1
            
            while i < ab.count && ab[i] == ab[i - 1] {
                count_ab += 1
                i += 1
            }
            
            while j < cd.count && cd[j] == cd[j - 1] {
                count_cd += 1
                j += 1
            }
            
            result += count_ab * count_cd
        } else if ab[i] + cd[j] > 0 {
            j += 1
        } else {
            i += 1
        }
    }
    
    print(result)
}