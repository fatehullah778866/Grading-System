print("Hello")
student_grading=int(input("enter the score: "))
if student_grading >=90 and student_grading<=100:
    print("Grade A")
    
elif student_grading>=80 and student_grading<=89:
    print("Grade B")
elif student_grading>=70 and student_grading<=79:
    print("Grade C")
elif student_grading>=60 and student_grading<=69:
    print("Grade D")
else:
    print("Grade F")

# git add .
# git commit -m "gradding system program"
# git push origin main