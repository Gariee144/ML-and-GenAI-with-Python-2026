length=float(input("enter length:"))
breadth=float(input("enter breadth:"))
area_rect=length*breadth
print(area_rect)

p=float(input("enter principal amount: "))
r=float(input("enter rate of interest per year: "))
t=float(input("enter time(in years): "))
simple_interest=p*r*t/100
print(simple_interest)

temp=float(input("enter temperature in celsius:"))
fahrenheit=temp*9/5 +32
print(fahrenheit)

a=float(input("enter first number: "))
b=float(input("enter second number: "))
c=float(input("enter third number: "))
average=(a+b+c)/3
print(average)

a=float(input("enter number: "))
square=a*a
cube=a*a*a
print("square of no. is:",square," ","cube of no. is: ",cube)

a=10
b=34
a,b=b,a
print("a is:",a,"   ","b is: ",b)


# Student Report Program
# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculate total marks
total = maths + science + english

# Calculate percentage
percentage = total / 3

# Display report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Maths Marks:", maths)
print("Science Marks:", science)
print("English Marks:", english)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
