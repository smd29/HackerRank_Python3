from itertools import combinations_with_replacement

word, size = input().split()
word = sorted(word)
size = int(size)


l = map("".join, list(combinations_with_replacement(word, size)))
for j in sorted(l):
    print(j)