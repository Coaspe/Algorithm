N = int(input())
string = input()
dna = {"A": 0, "C": 0, "G": 0, "T": 0}

for i in string:
    dna[i] += 1

min_val = min(dna.keys(), key=lambda x: dna[x])

print(dna[min_val])
print(N * min_val)
