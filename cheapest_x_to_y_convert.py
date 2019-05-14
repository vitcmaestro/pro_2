a,b = map(str,input("").split())
res = 0
check = min(a,b)
against = max(a,b)
i = 0
j = 0
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
print(diff+updates)
