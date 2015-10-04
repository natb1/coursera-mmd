permutation = [4, 6, 1, 3, 5, 2]
# convert to zero index
for i in range(len(permutation)):
    permutation[i] -= 1

table = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0]
]

def minhash(c):
    for i in permutation:
        value = table[i][c]
        if value == 1:
            return i

for c in range(4):
    print('C%s -> %s' % (c+1, minhash(c)+1))
