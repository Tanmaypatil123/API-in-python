num4=int(input())
print("enter the serial number to perform operation: ")
print("1] Reciprocal")
print("2] Square")
print("3] Square root")
choice=str(input("Enter the number of operation:"))
if (choice=='1'):
    print(1/num4)

elif (choice=='2'):
    print(num4**2)

elif (choice=='3'):
    print(num4**(1/2))
