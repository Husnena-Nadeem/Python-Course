# def disposCash(amount):
#     if amount%10 !=0:
#         return "invalid"
#     hundrad=amount//100
#     amount %=100
#     fifty=amount//50
#     amount%=50
#     Twenty=amount//20
#     amount%=20
#     if amount!=0:
#         return"return amount 100,50,20"
#     else:
#         return hundrad,fifty,Twenty

# amount=int(input("Enter the emount"))
# # disposCash(amount)
# # print(disposCash)

# result=disposCash(amount)
# print(result)



# import random

# attendance= [random.randint(50,100) for _ in range(100)]
# low_attendance=[]
# for i in range(100):
#     if attendance[i]<90:
#         low_attendance.append((i+1,attendance[i]))
# print("student attendence less then 90")

# for student , percent in low_attendance:
#         print(f"student{student}:{percent}%")

# print(f"Student attandence{len(low_attendance)}")




# movie={
#     "Movie 1":[2,3,4,5],
#     "Movie 2":[4,1,3,5],
#     "Movie 3":[5,5,4,2],
#     "Movie 4":[1,1,4,2],
#     "Movie 5":[1,1,5,5],
# }

# print("Movies reating.")

# highest=0
# topMovie=0

# for name,rating in movie.items():
#     avg=sum(rating)/len(rating)
#     print(f"{name},{round(avg)}")
#     if avg > highest:
#         highest=avg
#         topMovie=name

# print(f"Top movies:{topMovie},With reating",round(highest))




Employee=[range(20)]

print("Employee Enter your password:")
for Employee in  range(20):
    print(f"Enter the password:{Employee[i]}")
    password=int(input(F"Enter the password:"))
    if password==("@&!" or "123456789" or "alphabit"):
        print("Strong password:")
    elif password==( "123456789" or "alphabit"):
        print("Medion password:")
    elif password==("123456789"):
        print("Weak password")


    

