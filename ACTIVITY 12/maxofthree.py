def max_of_three(num1,num2,num3):
    """Return the largest of three n numbers numbers."""
    return max(num1,num2,num3)

def is_armstrong_number(number):
    """Returns True if the given number is a Armstrong number , False otherwise."""
    # convert the number to a string to find its length
    num_str=str(number)
    num_digits=len(num_str)

    #calculate the sum of each digit raised to the power of the number of didgit
    armstrong_sum=sum(int(digit)** num_digits for digit in num_str)

    #check if the sum i equal to the original number
    return armstrong_sum== number

#Example usage:
num1=153
num2=72
num3=987

#find the maximum of three numbers
max_value=max_of_three(num1,num2,num3)
print(f"The maximum of{num1},{num2}.and {num3} is:{max_value}")

#check if a number is an armstrong number
armstrong_num=153
non_armstrong_num=123

print(f"{armstrong_num} is armstrong: {is_armstrong_number(armstrong_num)}")
print(f"{non_armstrong_num} is armstrong: {is_armstrong_number(non_armstrong_num)}")
