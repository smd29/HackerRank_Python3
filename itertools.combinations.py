from itertools import combinations

word, size = input().split()
word = sorted(word)
size = int(size)

for i in range(1, size+1):
    l = map("".join, list(combinations(word, i)))

    for j in sorted(l):
        print(j)