import math
print("Choose the operation which you want do:")
print("1] Power(x^y)")
print("2] Root")
print("3] Factorial")
print("4] Logarithm")
print("5] trignometry")
print("6] absolute value(|x|)")
choice=int(input("Enter the serial number to perform action:"))
num5=int(input("Enter the number:"))

def power_raisedto(n):
    secnum=int(input("Enter the number :"))
    total2=pow(n,secnum)
    return total2

def power_root(n):
    secnum1=int(input("Enter the number:")) 
    total2=pow(n,1/secnum1)   
    return total2

def fact(n):
    total2=math.factorial(n)
    return total2

def log_with_base(n):
    secnum=int(input("enter the base of logarithm:"))  
    total2=math.log(n,secnum)
    return total2

def log_with_base10(n):
    total2=math.log10(n)
    return total2      

def absolute_value(n):
    return abs(n)    


if (choice==1):
    result=power_raisedto(num5)
    print(result)

elif(choice==2):
    result=power_root(num5)
    print(result)    

elif(choice==3):
    result=fact(num5)
    print(result)    

elif(choice==4):
    print("1]Log with other base")      
    print("2] log with base 10")
    choice2=int(input("Enter the serial number to perform action:"))
    if(choice2==1):
        print(log_with_base(num5))

    elif(choice2==2):
        print(log_with_base10(num5))

elif(choice==5):
    import trignometry            

elif(choice==6):
    print(absolute_value(num5))    