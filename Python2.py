##Write a program that will take three digits from the user
##and add the square of each digit

##num=int(input())
##num_str=str(num)
##sum_of_powers = 0
##for digit in num_str:
##    sum_of_powers += int(digit) ** 2
##print(sum_of_powers)

##Write a program that will take user input of (4 digits number) and
##check whether the number is narcissist number or not.

##def narcissist_number(num):
##    num_str=str(num)
##    num_len=len(num_str)
##    sum_of_numbers=sum(int(i) ** num_len for i in num_str)
##    return sum_of_numbers==num
##number=int(input())
##if narcissist_number(number):
##    print(f"{number} is narcissist_number")
##else:
##    print(f"{number} is not narcissist_number")

##Write a program that will give you the in hand salary after deduction of HRA(10%),
##DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),
##(11-20lakh–20%),(20<lakh-30%)(0-1lakh print k).

##def calculate_in_hand_salary(gross_sal):
##    hra = gross_sal * 0.10
##    da = gross_sal * 0.5
##    pf = gross_sal * 0.3
##    # Initial salary after HRA, DA, and PF deductions
##    salary_after_deductions = gross_sal - (hra + da + pf)
##
##    if gross_sal<100000:
##        tax=0
##        return 'k'
##    elif 500000<= gross_sal<= 1000000:
##        tax = 0.1 * gross_sal
##    elif 1100000<= gross_sal<= 2000000:
##        tax = 0.2 * gross_sal
##    elif gross_sal> 2000000:
##        tax = 0.3 * gross_sal
##    else:
##        tax = 0
##    #Final in-hand_salary after tax
##    in_hand_salary = salary_after_deductions - tax
##    return in_hand_salary
##
##gross_sal = float(input("Enter the gross salary: "))
##in_hand_salary = calculate_in_hand_salary(gross_sal)
##print(f"The in-hand salary is: {in_hand_salary}")

##Swapping of numbers
##a=int(input("Enter 1st number"))#1
##b=int(input("Enter 2nd number"))#2
##print(f"Before swap a = {a}, b = {b}")
##c=a #store value of a in c
##a=b #assign value of b in a
##b=c #assign the original value of a to b
##print(f"After swap a = {a}, b = {b}")

##Write a program that can multiply 2 numbers provided by
##the user without using the * operator

##import operator   
##a=int(input("Enter 1st number"))
##b=int(input("Enter 2nd number"))
##x=operator.mul(a,b)
##print(x)

##OR

##def multiply_without_asterisk(x, y):
##    result = 0    
##    # Multiply x by y by adding x to itself y times
##    for _ in range(abs(y)):  # Use abs(y) to handle both positive and negative numbers
##        result += x
##    
##    # Adjust the sign if y is negative
##    if y < 0:
##        result = -result    
##    return result
### Get input from the user
##a = int(input("Enter the first number: "))
##b = int(input("Enter the second number: "))
### Call the function and print the result
##product = multiply_without_asterisk(a, b)
##print(f"The product of {a} and {b} is: {product}")

##Write a program that can find the factorial of a given number provided by the user.
##def fact(f):
##    result=1
##    for i in range(2,f+1):
##        result=result*i
##    return result
##a=int(input())
##p=fact(a)
##print(p)

##Write a program to find the sum of first n numbers, where n will be provided by the user.
##Eg if the user provides n=10 the output should be 55.

##def sum_of_numbers(s):
##    result=0
##    for i in range(1,s+1):
##        result=result+i       
##    return result   
##n=int(input())
##p=sum_of_numbers(n)
##print(p)

##Identify even and odd numbers
##def odd_even_number(n):
##    if n%2!=0:
##        return 'odd'
##    else:
##        return 'even'
##n=int(input("Enter number"))
##o=odd_even_number(n)
##print(o)
