# display fibonicci series upto 10 numbers
#-------------------------------------------

num=10
n1,n2=0,1
print("Fibonicci series:",n1,end=" ")
for i in range(0,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n1,end=" ")
#print()
