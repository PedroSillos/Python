score_in = input("Enter the student's score")

try:
    score = float(score_in)
except:
    print("error, enter a number")
    quit()
    
if score < 0.0 or score > 1.0:
    print("score out of range")
    quit()
else:
    if score >= 0.9: grade = 'A'
    elif score >= 0.8: grade = 'B'
    elif score >= 0.7: grade = 'C'
    elif score >= 0.6: grade = 'D'
    else: grade = 'F'
print(grade)
