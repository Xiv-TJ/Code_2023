import math
import time
def get_average():
    total_marks = 0
    for subject in subjects:
        score = input(f"Input your {subject} marks here: ")
        if score.lower() != 'n':
            marks = float(score)
            total_marks += marks
            
    average = total_marks / len(subjects)
    rounded_average = math.floor(average)
    print(f"Your average marks are: {rounded_average}")

subjects = ["English", 
            "Mathematics", 
            "Science", 
            "History", 
            "Second Language", 
            "Geography", 
            "Literature", 
            "Social Studies", 
            "Computer Science", 
            "Music"]
print("Welcome to the Test Average Calculator! In this calculator, you will take note of ten subjects and your marks on them. This calculator will then calculate the average of these tests. Let's begin!")
time.sleep(10)
print("The subjects supported in this code is; English, Mathematics, Sceicne, History, Second Langauge, Geography, Litarature, Social Studies, COmputer Science and Music.")
time.sleep(10)
print("Of course, there are subjects that some people do not take. If you do not take said subject, please type them down here. You must seperate the subejcts with a comma.")
useless_subjects = input("Type the subjects you do not take here: ")
useless_subjects_list = useless_subjects.split(',')
for subject in useless_subjects_list:
    if subject.strip() in subjects:
        subjects.remove(subject.strip())
get_average()