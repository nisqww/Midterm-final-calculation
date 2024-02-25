
midterm_weight = int(input("What percentage will the midterm exam weigh in total grade? "))
final_weight = int(input("What percentage will the final exam weigh in total grade?"))
midterm_grade = int(input("Please enter your midterm grade: "))
final_grade = int(input("Please enter your final grade: "))

weighted_midterm = midterm_grade * midterm_weight/100
weighted_final = final_grade * final_weight/100
total_grade = weighted_midterm + weighted_final

print("Total weighted grade: ", total_grade)

if total_grade >= 50:
    print("You passed the course.")
else:
    print("You failed the course. ")

if 80<=total_grade<=100:
    print("AA")
elif 71<=total_grade<80:
    print("BA")
elif 63<=total_grade<71:
    print("BB")
elif 55<=total_grade<63:
    print("CB")
elif 50<=total_grade<55:
    print("CC")
elif 45<=total_grade<50:
    print("DC")
elif 35<=total_grade<45:
    print("DD")
elif 0<=total_grade<35:
    print("FF")


