a=int(input("Enter age: "))
if a<5:
    print("Free Ticket")
elif 5<=a<=12:
    ticket=200*0.5
    print("Ticket Price:",ticket)
elif 13<=a<=59:
    ticket=200
    print("Ticket Price:",ticket) 
else:  
    ticket=200*0.7
    print("Ticket Price:",ticket)