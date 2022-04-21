#Fibonacci time
#Hayden Hansen. Jan 15th, 2021

usernum = int(input("please input the amount of numbers of the sequence you would like: ", ))

#first two terms
num1, num2 = 0, 1
count = 0

if usernum <= 0:
    print("please enter a valid number")
elif usernum ==1:
    print("Fibonacci sequence up to", usernum, ":")
else:
    print("Fibonacci Sequence")
    while count < usernum:
        print(num1)
        temp = num1 + num2
        # update the numbers
        num1 = num2
        num2 = temp
        count += 1 
        
        
















