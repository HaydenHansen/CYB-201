# January 8, 2021
# Average numbers from an array, and also sorting numbers
#the numbers of the array are being added then divded by 8
def Average(fridayarray):
    return sum(fridayarray)/len(fridayarray)
    

fridayarray = [43, 27, 234, 4, 654, 654, 293, 848]

mysum = Average(fridayarray)
fridayarray.sort()

print("this is the average of the list: ", (mysum))
print("this list is sorted from lowest to highest ", (fridayarray))

