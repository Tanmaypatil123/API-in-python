import math
print("1]tan or tan inverse")
print("2] sin or sin inverse")
print("3] cos or cos inverse")
print("4] angle to radian ")
choice=int(input("Enter the serial number to perform action:"))
angle=int(input("Enter the angle:"))
def angle_to_radian(n):
    total=math.radians(n)
    return total

def tan_func(n):
    total=math.tan(n)
    return total 

def sin_func(n):
    total=math.sin(n)
    return total

def cos_func(n):
    total=math.cos(n)
    return total

def inverse_tan(n):
    return math.degrees(math.atan(n))

def inverse_sin(n):
    return math.degrees(math.asin(n))

def inverse_cos(n):
    return math.degrees(math.acos(n))
if(choice==1):
    print("1] tan")
    print("2] tan inverse")
    choice2=int(input("Enter the serial number :"))
    if(choice2==1):
        rad=angle_to_radian(angle)
        result=tan_func(rad)
        print(result)

    elif(choice2==2):
        n=int(input()) 
        result=inverse_tan(n)
        print(result)

elif(choice==2):
    print("1] sin ")
    print("2] sin inverse")
    choice2=int(input("Enter the serial number :"))      
    if(choice2==1):
        print(sin_func(angle))
    elif(choice2==2):
        n=int(input())
        print(inverse_sin(n))

elif(choice==3):
    print("1] cos ")
    print("2] cos inverse")
    choice2=int(input("Enter the serial number :")) 
    if(choice2==1):
        print(cos_func(angle))

    elif(choice2==2):
        n=int(input())
        print(inverse_cos(n))

elif(choice==4):
    print(angle_to_radian(angle))                         