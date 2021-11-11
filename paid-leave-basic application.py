"""
In this program, I will make simple joke of approval paid leave in the office
"""
manager = True
paid_leave = 3

print("I said to my Manager, 'Can I take my paid leave this month?")

if manager == True:
    print("My Manager say, 'Sure get a nice holiday for you!'")
    if paid_leave <= 3:
        print("My General Affair say, 'Yaps, your paid leave approved and happy holiday!'")
        print("Yippy I got my day!")
    else:
        print("My General Affair say, 'No Approved! Your paid leave is to much than your work days! Go Work!'")
        print("Work, work & work!")
else:
    print("My Manager say, 'No! Just get back to your desk and work!'")
    print("Work, work & work")


