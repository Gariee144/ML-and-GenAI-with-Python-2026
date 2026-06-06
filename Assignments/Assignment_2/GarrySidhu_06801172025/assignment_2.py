sum=0
for i in range(1,11):
    sum+=i

print("sum of natural no.:", sum)


fact=1
for i in range(1,5):
    fact*=i
print(fact)


n=10
a,b=0,1
for i in range(n):
    print(a," ")
    a,b=b,a+b

a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
c=float(input("enter the third number: "))
if a>=b and a>=c:
    print("largest number is:",a)
elif(b>=a,b>=c):
    print("largest number is: ",b)
else:
    print("largest number is: ",c)


name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total = 0
subjects = 5

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = total / subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)