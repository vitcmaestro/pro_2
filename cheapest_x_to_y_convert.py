def checker(check,against):
    i = 0
    j = 0
    res = 0
    while(i< len(check) and j< len(against)):
        if check[i] == against[j]:
            i+=1
            j+=1
        else:
            res+=1
            j+=1
    remi = len(check)-i
    remj = len(against)-i
    if(remi> remj):
        diff = remi - remj
        updates = remj
    elif(remi<remj):
        diff = remj-remi
        updates = remi
    else:
        diff = 0
        updates = remi
    return diff+updates
a,b = map(str,input("").split())
res1 = checker(min(a,b),max(a,b))
res2 = checker(max(a,b),min(a,b))
print(min(res1,res2))
