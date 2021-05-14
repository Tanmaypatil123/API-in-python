num1=int(input())
num2=int(input())
result=0
choice=str(input("Enter the operation to perform(+ & - & / & *):"))
if (choice=='+'):
    result+=num1+num2
    print(result)

elif (choice=='-'):
    result-=num1-num2
    print(result)

elif (choice=='/'):
    result=num1/num2
    print(result)

elif (choice=='*'):
    result=num1*num2   
    print(result)     

def addition(n,total):
    total+=n
    return total

def substraction(n,total):
    total-=n
    return total

def divison(n,total):
    total=total/n
    return total

def product(n,total):
    total=total*n
    return total            

while result:
    choice2=str(input("Enter the operation to perform(+ & - & / & * & stop):"))
    if (choice2=='+'):
        num3=int(input())
        result=addition(num3,result)
        print(result)

    elif (choice2=='-'):
        num3=int(input())
        result=substraction(num3,result)
        print(result)    

    elif (choice2=='/'):
        num3=int(input())
        result=divison(num3,result)
        print(result)

    elif (choice2=='*'):
        num3=int(input())
        result=product(num3,result)  
        print(result)      

    elif (choice2=='stop'):
        break
