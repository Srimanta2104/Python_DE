import Calc as c

#c.peoples("Srimanta","Vidya")

num1 = int(input("Enter first number: "))
num2= int(input("Enter second number: "))
choice = input("""
Please enter the choice as:
 + for addition
 - for subtraction
 * for multiplication
 / for division
""")
 
if choice == "+":
   c.addtion(num1,num2)
elif choice == "-":
     c.subract(num1,num2)
elif choice == "*":
     c.multiply(num1,num2)
elif choice == "/":
     c.division(num1,num2)
else:
    print("Wrong choice")
    print("""
Please enter the choice as:
 + for addition
 - for subtraction
 * for multiplication
 / for division
""")