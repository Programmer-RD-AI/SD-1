# Grade Calculation Program

# Get the scores from the user
coursework_score = float(input("Enter your coursework score (0-100): "))
midterm_score = float(input("Enter your midterm exam score (0-100): "))
final_exam_score = float(input("Enter your final exam score (0-100): "))

# Ensure the inputs are valid
if not (
    0 <= coursework_score <= 100
    and 0 <= midterm_score <= 100
    and 0 <= final_exam_score <= 100
):
    print("Error: Scores should be between 0 and 100.")
else:
    # Calculate weighted scores
    weighted_coursework = coursework_score * 0.40
    weighted_midterm = midterm_score * 0.25
    weighted_final_exam = final_exam_score * 0.35

    # Calculate final score
    final_grade = weighted_coursework + weighted_midterm + weighted_final_exam

    # Determine letter grade
    if final_grade >= 70:
        letter_grade = "A"
    elif final_grade >= 50:
        letter_grade = "B"
    elif final_grade >= 40:
        letter_grade = "C"
    else:
        letter_grade = "F"

    # Display the final grade and letter grade
    print(f"Final numeric grade: {final_grade:.2f}")
    print(f"Final letter grade: {letter_grade}")
