# Calculator in python
# Your program should take operator and the two numbers as input from the user and then return the result

print("Welcome! To Calculator made by Coded Pirater!")
Operators = "* ,  + , / , - , ** "
print("List of operation which you can perform here: \n", Operators)
Operator1 = "+"
Operator2 = "*"
Operator3 = "/"
Operator4 = "-"
Operator5 = "**"
num1 = (input("Enter Your First Number :"))
Operator = (input("Enter Your Operator :"))
num2 = (input("Enter Your Second Number :"))

if Operator1==Operator:
    print("Your ansewr is = ",int(num1)+int(num2))
elif Operator2==Operator:
    print("Your answer is = ",int(num1)*int(num2))
elif Operator3==Operator:
    print("Your answer is = ",int(num1)/int(num2))
elif Operator4==Operator:
    print("Your answer is = ",int(num1)-int(num2))
elif Operator5==Operator:
    print("Your answer is = ",int(num1)**int(num2))
else:
    print("Error!, Please ckeck your numbers and operator and Try Again! ")