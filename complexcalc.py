print("welcome : Complex calculator")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = int('first_number')
num2 = int('second_number')
operator = input("Enter operator: ")
ans = "answer="
if '+' ==operator:
    print(ans,first_number+second_number)
elif '*' ==operator:
    print(ans,first_number*second_number)
elif '/'==operator:
    print(ans,first_number/second_number)
elif '%' ==operator:
    print(ans,first_number%second_number)
else:
    print("operator does not exist")