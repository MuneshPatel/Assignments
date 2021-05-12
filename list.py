x=int(input("Enter the number of elements of list :"))
i=0
j=0
list=[]
print("Enter the elements of the list :")
while i<x :
    list.append(input())
    i+=1
while j<x :
    if int(list[j])>0 :
        print(list[j],",",end=" ")
    j+=1
