'''
* *  * *      
*      *
*      *
*      *
* * *  * 
'''  
num=int(input("enter num"))
for i in range(1,num):
    for j in range(1,num):
        if j!=1 and j!=(num-1) and i!=1 and i!=(num-1): 
         print(".",end="")
        else:
           print("*",end="")
           
           #other condition 

        # if i==1 or i==(num-1) or j==1 or j==num-1:
        #     print("*",end="")
        # else:
        #     print(".",end="")
    print()

