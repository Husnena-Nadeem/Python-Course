marks=int(input("Enter your marks:\t"))

if(marks>=33):
    
    if(marks>=90):
        print("Grade 'A':")

    elif(marks>=80):
        print("Grade 'B':")
    
    elif(marks>=70):
        print("Grade 'C':")

    else:
        print("Student is pass but no specific grade")    
       
else:
    print("Fail")



print("End of program")  