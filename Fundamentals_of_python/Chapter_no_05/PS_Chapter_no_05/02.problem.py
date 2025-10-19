marks1 = int(input("Enter the first Number1: "))
marks2 = int(input("Enter the first Number2: "))
marks3 = int(input("Enter the first Number3: "))

total_percentage = (100 * (marks1 + marks2 + marks3)) / 300
# total_percentage=(marks1+marks2+marks3)/3

if (total_percentage >= 40 and marks1 >= 40 and marks2 >= 40 and marks3 >= 40):
    print("You are passed:", total_percentage)
else:
    print("You are failed, please try again:", total_percentage)
