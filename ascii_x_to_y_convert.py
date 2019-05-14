a,b = map(str,input().split())
res = 0
i = 0
while i <(len(min(a,b))):
    if(ord(a[i])>ord(b[i])):
        diff = ord(a[i])-ord(b[i])
    elif(ord(b[i])>ord(a[i])):
        diff = ord(b[i])-ord(a[i])
    else:
        diff = 0
    res = res+ diff
    i+=1
rem = max(a,b)
for j in range(i,len(rem)):
    res += ord(rem[j].lower())-96
print(res)
