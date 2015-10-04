def two_shingles(s):
    shingles = set()
    for i in range(len(s) - 1):
        shingles.add(s[i:i+2])
    return shingles

shingles1 = two_shingles('ABRACADABRA')
shingles2 = two_shingles('BRICABRAC')

print('in common %s' % (len(shingles1 & shingles2)))
print('shingles1 %s' % (len(shingles1)))
