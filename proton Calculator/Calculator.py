print("Choose type of calculator:")
print("1] Standard")
print("2] Scientific")
print("3] Age calculator")
wth=int(input("Enter the number here to perform action:"))
if(wth==1):
    print("Enter the operation serial number:")
    print("1] reciprocal , square , sqroot")
    print("2] addition , substraction, division, multiplication")
    choice=str(input("Enter the serial number to perform operation(1 & 2):"))
    if (choice=='1'):
        import oistandard

    elif (choice=='2'):
        import distandard 

elif(wth==2):
    import scientific           

elif(wth==3):
    import age_calculator
