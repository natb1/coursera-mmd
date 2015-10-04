options = [
    (55, 5),
    (66, 5),
    (52, 13),
    (56, 13)
]

import math 

def l1(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def l2(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

for option in options:
    l1a = l1(option, (0, 0))
    l1b = l1(option, (100, 40))
    l2a = l2(option, (0, 0))
    l2b = l2(option, (100, 40))
    l1closest = 'a' if l1a < l1b else 'b'
    l2closest = 'a' if l2a < l2b else 'b'
    print('%s l1 == l2 %s' % (option, l1closest == l2closest))

