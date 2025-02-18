a = 'aaabb1111ccccc'
mdict = {}
j = 1
som = 0
for i in range(len(a)):
    if a[i] not in mdict.keys():
        som = 1
    else:
        som += 1
    mdict[a[i]] = som
    
    
print(mdict) 