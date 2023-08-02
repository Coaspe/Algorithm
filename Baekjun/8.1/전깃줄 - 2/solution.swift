import Foundation

// MARK: - Thanks to Wapas

final class FileIO {
    
    private let buffer:[UInt8]
    private var index: Int = 0

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        buffer = Array(try! fileHandle.readToEnd()!)+[UInt8(0)]
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }

        return buffer[index]
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true
        while now == 10 || now == 32 { now = read() }
        if now == 45 { isPositive.toggle(); now = read() }
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1 : -1)
    }

    @inline(__always) func readString() -> String {
        var now = read()
        while now == 10 || now == 32 { now = read() }
        let beginIndex = index-1
        while now != 10, now != 32, now != 0 { now = read() }

        return String(bytes: Array(buffer[beginIndex ..< (index-1)]), encoding: .ascii)!
    }
    
    @inline(__always) func readStirngSum() -> Int {
        var byte = read()
        while byte == 10 || byte == 32 { byte = read() }
        var sum = Int(byte)
        while byte != 10 && byte != 32 && byte != 0 { byte = read(); sum += Int(byte) }
        
        return sum - Int(byte)
    }
}

// MARK: - Input

typealias Connection = (lhs: Int, rhs: Int)

let fileIO = FileIO()
let numberOfPowerCord = fileIO.readInt()
var connections = Array(repeating: Connection(0, 0), count: numberOfPowerCord)
for index in 0 ..< numberOfPowerCord {
    connections[index] = (fileIO.readInt(), fileIO.readInt())
}
connections.sort { $0.lhs < $1.lhs }
print(solution(numberOfPowerCord, connections))

// MARK: - Solutions

private func binarySearch(_ connections: [Connection], _ start: Int, _ end: Int, _ target: Int) -> Int? {
    if end <= start {
        return end
    } else {
        let mid = (start + end) / 2
        if target < connections[mid].rhs {
            return binarySearch(connections, start, mid, target)
        } else if target == connections[mid].rhs {
            return nil
        } else {
            return binarySearch(connections, mid + 1, end, target)
        }
    }
}

private func solution(_ numberOfPowerCord: Int, _ connections: [Connection]) -> String {
    var answer = ""
    var cords: [Connection] = []
    var cordsToCut: [Int] = []
    var indicesOfCords: [(connection: Connection, index: Int)] = []
    for connection in connections {
        if cords.isEmpty {
            cords.append(connection)
            indicesOfCords.append((connection, 0))
        } else {
            if let last = cords.last, last.rhs < connection.rhs {
                cords.append(connection)
                indicesOfCords.append((connection, cords.count - 1))
            } else {
                if let targetIndex = binarySearch(cords, 0, cords.endIndex - 1, connection.rhs) {
                    cords[targetIndex] = connection
                    indicesOfCords.append((connection, targetIndex))
                }
            }
        }
    }
    indicesOfCords.reverse()
    var current = cords.count - 1
    for indexOfCord in indicesOfCords {
        if indexOfCord.index == current {
            current -= 1
        } else {
            cordsToCut.append(indexOfCord.connection.lhs)
        }
    }
    cordsToCut.sort()
    answer += "\(cordsToCut.count)\n"
    for cord in cordsToCut {
        answer += "\(cord)\n"
    }
    let _ = answer.popLast()
    
    return answer
}