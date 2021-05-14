import datetime
today1=datetime.date.today()
print("Today's date=",today1)
bdate=int(input("Enter date of birth(only date nor month or year):"))
print("Choose the serial number of month of your birth:")
print("1] JANUARY")
print("2] FEBRUARY")
print("3] MARCH")
print("4] APRIL")
print("5] MAY")
print("6] JUNE")
print("7] JULY")
print("8] AUGUST")
print("9] SEPTEMBER")
print("10] OCTOBER")
print("11] NOVEMBER")
print("12] DECEMBER")
bmonth=int(input("enter the serial number here:"))
byear=int(input("Enter the year of birth:"))
birth=datetime.date(byear,bmonth,bdate)
print("Date of birth:",birth)
days=today1-birth
print(days)

from datetime import date

def calculateAge(birthDate):
	today = date.today()
	age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))

	return age
	
print(calculateAge(birth),"years")

