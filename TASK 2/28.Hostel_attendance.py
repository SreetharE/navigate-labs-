A=int(input("Attendance percentage:"))
if A>=75:
    print("Fine not applicable")
else:
    fine=(75-A)*10
    print("Fine amount:",fine)