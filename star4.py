'''   *
      *
* * * * * * *
      *
      *
      *
'''
num=int(input("enter num"))
   
for i in range(1,num):
    for j in range(num):
        if num%2!=0:
         if j!=(num-1)/2 and i!=(num-1)/2:
            print(" ",end="")
         else:
            print("*",end="")
        else:
           if j!=(num)/2 and i!=(num)/2:
            print(" ",end="")
           else:
            print("*",end="")
    print()