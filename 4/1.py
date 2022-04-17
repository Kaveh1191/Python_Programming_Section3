"""
Kaveh Masoudinia
Section 3 Exercise 4
"""
import random

G_count=True
a=random.randint(1,10)
b=random.randint(1,10)
while G_count==True:

    print("How much is",a,"times",b,"?")
    ans=int(input("Your answer:"))
    if ans==a*b:
        print("very good")
        break
    elif ans!=a*b:
        print("No,please try again")
        print("How much is", a, "times", b, "?")
        ans = int(input("Your answer:"))
        if ans==a*b:
            print("very good")
            break
