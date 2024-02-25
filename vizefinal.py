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