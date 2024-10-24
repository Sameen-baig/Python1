##check palindrome
##class Solution:
##    def isPalindrome(self, x: int) -> bool:
##        # Negative numbers are not palindromes
##        if x < 0:
##            return False
##        
##        # Numbers ending in 0 that are not 0 are not palindromes
##        if x % 10 == 0 and x != 0:
##            return False
##
##        reversed_half = 0
##        while x > reversed_half:
##            reversed_half = reversed_half * 10 + x % 10
##            x //= 10
##
##        # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
##        return x == reversed_half or x == reversed_half // 10
##
### Example usage
##sol = Solution()
##print(sol.isPalindrome(121))  # Output: True
##print(sol.isPalindrome(-121)) # Output: False
##print(sol.isPalindrome(10))   # Output: False
##print(sol.isPalindrome(12321))# Output: True

#check armstrong_number
##def is_armstrong_number(num):
##    # Convert the number to a string to easily iterate over digits
##    num_str = str(num)
##    # Get the number of digits in the number
##    num_digits = len(num_str)
##    print(num_digits)
##    # Calculate the sum of each digit raised to the power of the number of digits
##    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
##    # Check if the sum of powers is equal to the original number
##    return sum_of_powers == num

### Example usage
##number = 1634
##if is_armstrong_number(number):
##    print(f"{number} is an Armstrong number.")
##else:
##    print(f"{number} is not an Armstrong number.")

##Write a program that will take three digits from the user and
##add the square of each digit
##num=int(input())
##num_str=str(num)
##sum_of_powers = 0
##for digit in num_str:
##    sum_of_powers += int(digit) ** 2
##print(sum_of_powers)

##Write a menu driven program - 1.cm to ft  2.kl to miles 3.usd to inr 4.exit
##def menu_driven(usr_input,num):   
##    if usr_input == 1:
##        return num * 0.0328084
##        
##    elif usr_input == 2:
##        return num * 0.621371
##        
##    elif usr_input == 3:
##        return num * 278.71
##    else:
##        return "Invalid choice"
##def main():
##    while True:
##        print("\nMenu:")
##        print("1. Convert cm to ft")
##        print("2. Convert km to miles")
##        print("3. Convert USD to PKR")
##        print("4. Exit")
##        
##        usr_input = int(input())
##
##        if usr_input == 4:
##            print("Exit")
##            break
##        num = float(input("Enter a number"))
##        result = menu_driven(usr_input,num)
##        print(f"the result of conversion is {result}")
##if __name__=="__main__":
##    main()

##Write a program to print the first 25 odd numbers
##def print_odd_numbers(n):
##    count = 0 #count keeps track of how many odd numbers have been printed.
##    number = 1 #number starts at 1, which is the first odd number.
##    while count < n:
##        print(number, end=" ")
##        number += 2  # Move to the next odd number
##        count += 1
##
### Call the function to print the first 25 odd numbers
####n=25
##n=int(input())
##p=print_odd_numbers(n)
##print(p)

##The current population of a town is 10000. The population of the town is increasing
##at the rate of 10% per year. You have to write a program to find out the population
##at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
##10th year - 10000
##9th year - 9000
##8th year - 8100 and so on

##p=10000
##g=0.1
##for i in range(1,11):
##    print(f"{11 - i}th year - {int(p)}")
##    p=p//(1+g)
    
##Write a program that will tell the number of dogs and chicken
##are there when the user will provide the value of total heads and legs.

##def cats_dogs(heads,legs):
##    if legs % 2 != 0:
##        return "Invalid input: total legs must be even."
##    #calculate the number of cats and dogs
##    cats=(2*heads-legs//2)
##    dogs=heads-cats
##
##    # Validate the results
##    if cats<0 or dogs<0:
##        return "Invalid input: Negative number of animals."
##
##    return int(cats), int(dogs)
## 
##heads = int(input("Enter the total number of heads: "))
##legs = int(input("Enter the total number of legs: "))
##result=cats_dogs(heads,legs)
##print(result)


##Write a program that will determine weather when the value of temperature and humidity is provided by the user.
##TEMPERATURE(C)  HUMIDITY(%)      WEATHER
##
##
## >= 30    >=90        Hot and Humid
##
## >= 30    < 90        Hot
##
## <30      >= 90       Cool and Humid
##
## <30      <90         Cool
##provide humidity,temp and return weather

##def weather(temp,humid):
##    if temp >=0 and 0 <= humid <= 100: 
##        if temp<30 and humid<90:
##            return 'Cool'
##        elif temp<30 and humid>=90:
##            return 'Cool and Humid'
##        elif temp>=30 and humid<90:
##            return 'Hot'
##        elif temp>=30 and humid>=90:
##            return 'Hot and Humid'
##        else:
##            return "Invalid Input"
##    else:
##        return 'Invalid Input'
##
##temp=int(input("Enter the value of temperature"))
##humid=int(input("Enter the value of humidity"))
##w=weather(temp,humid)
##print(w)


##A = ['1','2','3']
##for a in A:
##    print(2*a)

##Consider the function add, what is the result of calling the following Add('1','1') (look closely at the return statement )

def Add(x,y):
    z=y+x
    return(y)

z=Add('1','1')
print(z)
















        
