var T = Int(readLine()!)!

while T > 0 {
    T -= 1
    let n = Int(readLine()!)!

    var B = Array(repeating: 0, count: 5)
    var six: Int = n / 60, tens = (n % 60) / 10, ones = n % 10

    if ones > 5 {
        ones -= 10
        tens += 1
    }

    if tens > 3 {
        tens -= 6
        six += 1
    }

    if ones == 5, tens < 0 {
        tens += 1
        ones = -5
    }

    B[0] = six
    B[2 - (tens >= 0 ? 1 : 0)] = abs(tens)
    B[4 - (ones >= 0 ? 1 : 0)] = abs(ones)

    print(B.map { String($0) }.joined(separator: " "))
}
