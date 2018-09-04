def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1;
    else:
        return (x * calc_factorial(x-1));

num = input("Enter a number : ");
num = int(num);
print("The factorial of", num, "is", calc_factorial(num))