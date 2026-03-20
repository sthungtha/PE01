# 1. Create a list of test scores
scores = [85, 92, 78, 90, 88]
print("Scores list created:", scores)


# 2. Calculate the average score using floor division
total_score = sum(scores)
num_tests = len(scores)
average_score = total_score // num_tests
print("Average score calculated using floor division:", average_score)


# 3. Determine the grade using comparison operators
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade determined using comparison operators:", grade)


# 4. Update the grade using assignment operators
if average_score % 10 >= 5:
    grade += "+"
else:
    grade += ""   # explicit else added

print("Grade after assignment operator update:", grade)


# 5. Membership operator check
check_score = 90
if check_score in scores:
    print(f"The score {check_score} exists in the list.")
else:
    print(f"The score {check_score} does not exist in the list.")


# 6. Identity operator comparison
scores_copy = scores
if scores is scores_copy:
    print("scores and scores_copy are the SAME object.")
else:
    print("scores and scores_copy are DIFFERENT objects.")


# 7. Bitwise AND operation
bitwise_result = scores[0] & scores[1]
print(f"Bitwise AND of the first two scores ({scores[0]} & {scores[1]}): {bitwise_result}")


# 8. Final output
print(f"\nFinal Result → Average: {average_score}, Grade: {grade}")
