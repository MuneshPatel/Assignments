frequency={}
x=input("Enter the word :").lower()
for i in x:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1

print(sorted(frequency.items(),key= lambda kv:(kv[1],kv[0]),reverse=True))
