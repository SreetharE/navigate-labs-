cgpa=float(input("Enetr CGPA:"))
attendance=int(input("Enter attendance percentage:"))
arrears=int(input("Enter number of arrears:"))
if cgpa>=7.5 and attendance>=75 and arrears==0:
    print("Eligible for loan")
else:
    print("Not eligible for loan")