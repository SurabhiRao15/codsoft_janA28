print("   CALCULATOR   ")
num1=float(input("Enter first number = "))
num2=float(input("Enter second number = "))
print("Enter 1 for addition.")
print("Enter 2 for subtraction.")
print("Enter 3 for multiplication.")
print("Enter 4 for division.")
print("Enter 5 for modulus.")
add= num1+num2
sub= num1-num2
product= num1*num2
quotient= num1/num2
modulus= num1%num2
choice=int(input("Enter your choice 1/ 2/ 3/ 4/ 5 = "))

if choice==1:
    print("Sum = ", add)
elif choice==2:
    if num1<num2:
        print("You will get a negative number = ",sub)
    else:
        print("Subtraction = ", sub)

elif choice==3:
    print("Product = ", product)
elif choice==4:
    if num1==0:
        print("Zero Division Error. The numerator should not be zero.")
    else:
        print("Quotient = ", quotient)

elif choice==5:
    print("Modulus = ", modulus)
else:
    print(" Invalid Choice ")

print("   Thank you   ")

