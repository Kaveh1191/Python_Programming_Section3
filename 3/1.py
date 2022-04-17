"""
Kaveh Masoudinia
Section 3 Exercise 3
"""
import random

count=3
G_count=True
while G_count==True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a,'*',b,'=?')
    ans=int(input("Your answer:"))
    if ans==a*b:
        count+=1
        print("You win!!!")
    elif ans!=a*b:
        count-=1
        print("you lose")
        if count==0:
            print("You lose game!!!")
            break
    G_count=input("Do you want to countinue?(Yes or No)")
    if G_count=='yes'or G_count=='Yes':
        G_count=True
    elif G_count=='No'or G_count=="no":
        G_count=False
        break

