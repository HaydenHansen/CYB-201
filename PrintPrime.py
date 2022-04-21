# print out prime numbers from one to 100
# Hayden Hansen
# january 8, 2021

begin = 1
end = 10

for i in range(begin, end):
    for j in range(2,i):
        if(i % j == 0):
            break
        else:
            print(i)
