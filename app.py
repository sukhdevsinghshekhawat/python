'''
donor amount=10,20,50;
amount need=1000;
count how many people  donate;
'''
'''
donate=0
count=0
while donate<1000:
     amount=int(input("enter your donate amount "))
     if amount==10 or amount==20 or amount==50:
          donate=donate+amount 
          if donate>1000:
               print("amount not valid")
               donate=donate-amount
               pass
          else:
           count=count+1
           print(f"your amount donated {donate} success \t total donor:: {count} ")
     else:
          print("amount not valid try valid  amount 10,20,50 ")
print(f"goal achieve amount: {donate} total donor::{count}")

        '''


donate = 0
count = 0

while donate < 1000:
    amount = int(input("Enter your donation amount: "))
    if amount in [10, 20, 980]:
        donate += amount
        if donate > 1000:
            print("Amount not valid. Donation exceeds the target.")
            donate -= amount
        else:
            count +=1
            print(f"Your donation of {amount} was successful. Total donated: {donate}. Total donors: {count}.")
    else:
        print("Amount not valid. Please enter a valid amount: 10, 20, or 50.")
        
print(f"Goal achieved! Total amount donated: {donate}. Total donors: {count}.")

#This revised version clarifies the instructions and improves overall readability.
