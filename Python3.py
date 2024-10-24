##Print first 25 prime numbers(1,2, 3, 5, 7, 11, 13..
##def is_prime(n):
##    if n <= 1:
##        return False
##    for i in range(2, int(n**0.5) + 1):
##        if n % i == 0:
##            return False
##    return True
##
##def print_primes(limit):
##    for num in range(2, limit + 1):
##        if is_prime(num):
##            print(num, end=" ")
##
### Set the limit up to which you want to print prime numbers
##limit = int(input("Enter the limit: "))
##
### Call the function to print prime numbers up to the limit
##print_primes(limit)

##Take a number from the user and find the number of digits in it
##n=int(input())
##s=str(n)
##digits=len(s)
##print(digits)

##Write a program that keeps on accepting a number from the user until
##the user enters Zero.Display the sum and average of all the numbers.

##def calculate_sum_and_average():
##    total_sum = 0
##    count = 0
##
##    while True:
##        num = float(input("Enter a number (enter 0 to stop): "))
##        
##        if num == 0:
##            break

##total_sum keeps track of the sum of all the entered numbers.
##count keeps track of how many numbers were entered.
##        total_sum += num
##        count += 1
##    
##    if count == 0:
##        print("No numbers were entered.")
##    else:
##        average = total_sum / count
##        print(f"Sum of all numbers: {total_sum}")
##        print(f"Average of all numbers: {average}")
##
### Call the function to start the process
##calculate_sum_and_average()

##Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
##Eg if the num = 5, den = 15 the answer should be ⅓
##Eg if the num = 6, den = 9 the answer should be ⅔

##import math
##def simplify_fraction(numerator, denominator):
##    # Find the greatest common divisor (GCD) of the numerator and denominator
##    gcd = math.gcd(numerator, denominator)
##    
##    # Divide both numerator and denominator by their GCD
##    simplified_numerator = numerator // gcd
##    simplified_denominator = denominator // gcd
##    
##    return simplified_numerator, simplified_denominator
##
### Input from the user
##numerator = int(input("Enter the numerator: "))
##denominator = int(input("Enter the denominator: "))
##
### Simplify the fraction
##simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
##
### Display the result
##if simplified_denominator == 1:
##    print(f"The simplified fraction is: {simplified_numerator}")
##else:
##    print(f"The simplified fraction is: {simplified_numerator}/{simplified_denominator}")

def string_length(s,c):
    count = 0
    for char in s:
        if char==c:
            count += 1
    return count

# Get input from the user
input_string = input("Enter a string: ")
c=input("e")
# Find and print the length of the string
length = string_length(input_string,c)
print(f"The length of the string is: {length}")






