# x = int(input("enter first number(x): "))
# y = int(input("enter second number(y): "))

# # if x>0:
# #     print("first number is a positive number")
# # elif x<0:
# #     print("first number is a negative number")
# # else:
# #     print("0 is neither positive nor negative")

# # if x>y:
# #     print(x," is the greater than ",y)
# # elif x<y:
# #     print(y," is the greater than ",x)
# # else:
# #     print("both are equal numbers")

# print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# if choice == '1':
#     print(x+y)
# elif choice == '2':
#     print(x-y)
# elif choice == '3':
#     print(x*y)
# elif choice == '4':
#     print(x/y)
# else:
#     print("Invalid input")

score = int(input("Enter your score: "))

if score >= 50:
    print("You passed the exam.")

    if score >= 90:
        print("Your grade is A.")
    elif score >= 75:
        print("Your grade is B.")
    elif score >= 60:
        print("Your grade is C.")
    else:
        print("Your grade is D.")
else:
    print("You failed the exam.")
