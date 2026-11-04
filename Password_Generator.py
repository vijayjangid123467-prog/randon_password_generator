
print("WELCOME TO PASSWORD GENERATOR")
print("You can generate random password")

l=int(input("enter length of password:"))

i=1
while i<=l:
    import random
    n=random.randint(0,9)
    print(f"Digit({i})={n}")
    i+=1