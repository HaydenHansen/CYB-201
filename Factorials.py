# Hayden Hansen, Jan 13, 2020
# factorials

usernum=int(input("please input a positive whole number to compute a factorial:", ))

def factorial(usernum):
    if usernum == 0:
        return 1
    else:
        return usernum * factorial(usernum-1)

print(factorial(usernum))









    
