# Write a python program to swap two numbers without using a temporary(third) variable

num1=int(input("Enter any 1st number:"))
num2=int(input("Enter any 2nd number:"))
print(f"Before swapping {num1} and {num2}")
num1,num2=num2,num1
print(f"After swapping value {num1} and {num2}")


# Write a python program to take input username and age and print also
username=input("Enter any username:")
age=int(input("Enter any age:"))
print("Username:",username)
print("Age:",age)


# Q3 Write a python program to convert string "123" to int and float
str="123"
print("Converted integer value:",int(str))
print("Converted float value:",float(str))



#Q4. Write a python program to find the largest of three numbers using if else statement
num1=int(input("Enter any 1st number:"))
num2=int(input("Enter any 2nd number:"))
num3=int(input("Enter any 3rd number:"))


# Q. Write a python program to print the Fibonacci series in python
n=int(input("Enter the term value:"))
a,b=0,1
print("Fibonacci Series:")
for i in range(n):
    print(a,end=" ")
    a, b=b, a+b



# Q5. Write a python program to find the sum of digits of a number
num=int(input("Enter any number:"))
total=0
while num>0:
  digit=num%10
  total+=digit
  num//10
print("Sum of digit:",sum)


# Q. Write a python program to find the square and cube of a number using function
def func(num):
  if num>0:
    print(f"Square of {num} :",(num**2))
    print(f"Qube of {num} :",(num**3))
  else:
    print(f"Not possible Qube and square of {num} :",num)
nu=int(input("Enter any number:",func(nu)))

