#Hayden Hansen - GCU budget calc
#import date functions
from datetime import date, time, datetime
count = 0
while (count < 1):
    today = date.today()
#inputs for day leaving, and then the day student is leaving bucket
    x = int(input("please enter the year you will be leaving: ", ))
    y = int(input("please enter the month you will be leaving: ", ))
    z = int(input("please enter the day you will be leaving: ", ))
    LeaveDay = date(x,y,z)

#calcs amount of days left based upon todays date and the day the student is leaving
    DaysLeft = LeaveDay - today

#amount they have left, in float format for division with cents
    Money = float(input("please input how many dining dollars you have left: ", ))

#finally the amount of money they have left, Days Left needs the float aspect in order to maintain the correct
#division and also the .days addition to convert the days left from time into an int
    MoneyPerDay = Money/ float(DaysLeft.days)

    print("you can spend:",MoneyPerDay, "dollars a day for the remaining",DaysLeft.days,"days until you leave")

