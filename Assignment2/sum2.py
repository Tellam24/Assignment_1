# accept numbers till user enters 0 and display the total of all the numbers entered.
#---------------------------------------------------------------------------------
lst=[]
while(True):
    n=int(input("Enter a number:"))
    if n==0:
        break
    else:
        lst.append(n)
if (len(lst)==0):
    print("list is empty ")
else:
    x=0
   
    for i in lst:
        x+=i
        i+=1

    else:
        print(x) 


    