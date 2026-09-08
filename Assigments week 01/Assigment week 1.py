# Celsius to Fahrenheit Converter

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# Area of a Rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of the rectangle:", area)


#compound interset calculate
p=float(input("Enter principle Amount:"))
R=float(input("Enter Rate on interest (%):"))
T=float(input("Enter time(years):"))
CI=p*(1+R/100)**T-p
print("coumpound interest:",CI)

#perimeter of a rectangular
length=float(input("Enter the length:"))
width=float(input("Enter the width:"))
perimeter=2*(length+width)
print("perimeter of the rectangle:",perimeter)



#Average of three numbers
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

average=(num1+num2+num3)/3
print("Average:",average)



#square and cube of a number
number=float(input("Enter a number"))
square= number**2
Cube= number**3
print("square:",square)
print("cube:",Cube)

#Distribute item equally
candies=int(input("Enter the number of candies:"))
students=int(input("Enter the number of students:"))
each_student=candies//students
left_candies= candies%students
print("Each student gets:",each_student)
print("candies left:",left_candies)


#calculate the profit and loss
cost_price=float(input("Enter cost price:"))
selling_price=float(input("Enter selling :"))
if selling_price>cost_price:
    profit=selling_price - cost_price
    print("profit:", profit)
elif cost_price>selling_price:
    loss=cost_price - selling_price
    print("loss:", loss)
else:
    print("No profit no loss")

#total marks,percentage and average 
sub1=float(input("Enter marks of subject 1:"))
sub2=float(input("Enter marks of subject 2:"))
sub3=float(input("Enter marks of subject 3:"))
sub4=float(input("Enter marks of subject 4:"))
sub5=float(input("Enter marks of subject 5:"))

total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
average=total/5

print("total marks:",total)
print("percentage:",percentage)
print("Average:", average)


#salary calculator
basic_salary=float(input("Enter Basic salary:"))
hra=basic_salary*20/100
da=basic_salary*15/100
total_salary=basic_salary+hra+da
print("Basic salary:",basic_salary)
print("HRA (20%):",hra)
print("DA(15%):",da)
print("Total salary:", total_salary)



#age in months and days
age=int(input("Enter your age in years"))
months=age*12
days=age*365
print("Age in months:",months)
print("Age in days (Approx):", days)



#currency converter (Usd to pkr)
usd=float(input("Enter amount in USD:"))
exchange_rate=285 
pkr=usd*exchange_rate
print("Amount in pkr:", pkr)


#sum of first N Natural numbers
n=int(input("Enter a number:"))
sum=n*(n+1)/2
print("sum of first", n, "natural numbers is:", sum)

#percentage of correct answer
total_questions=int(input("Enter total questions:"))
correct_answers=int(input("Enter correct answer:"))
percentage=(correct_answers/total_questions)*100
print("percentage score:",percentage,"%")


#speed distance time
distance=float(input("Enter Distance:"))
time=float(input("Enter time:"))
speed=distance/time
print("speed:",speed)



#calculate body mass index (BMI)
weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))
bmi=weight/(height**2)
print("BMI:",bmi)


#convert mintues to hours and mintues
mintues=int(input("Enter total mintues:"))
hours=mintues//60
remaining_mintues=mintues%60
print("Hours:", hours)
print("Remaining Mintues:", remaining_mintues)


