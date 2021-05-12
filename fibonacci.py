i=0
j=1
s=0
z=1
x=int(input("Enter the number of terms to be displayed :"))
print("The fibonacci series is :")
print(i,",",j,end=" ")
while z<=(x-2) :
    s=i+j
    print(",",s,end=" ")
    i=j
    j=s
    z+=1
