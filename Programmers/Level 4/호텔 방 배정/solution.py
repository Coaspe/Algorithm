from sys import setrecursionlimit

setrecursionlimit(2 * 10**5 + 1)


def solution(k, room_number):
    answer = []
    allocated = {}

    def find(room):
        print(room)
        if room not in allocated:
            allocated[room] = room + 1
            return room
        allocated[room] = find(allocated[room])
        return allocated[room]

    for room in room_number:
        print("ROOM", room)
        available = find(room)
        answer.append(available)

    return answer
