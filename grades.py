def main():
    # Print introduction message
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    # print blank line
    print()

    # Get midterm 1 information
    midterm1_weight = get_weight("Midterm 1:")
    midterm1_score = get_score("Midterm 1")
    midterm1_shifted = get_shift()
    if midterm1_shifted == 1:
        midterm1_score += get_shift_amount()
        midterm1_score = min(100, midterm1_score)
        print(f"Total points = {midterm1_score} / 100")
        weighted_1 = round((midterm1_score / 100)*(midterm1_weight), 1)
        print(f"Weighted score = {weighted_1} / {midterm1_weight}")
        print()
    else:
        print(f"Total points = {midterm1_score} / 100")
        weighted_1 = round((midterm1_score / 100)*(midterm1_weight), 1)
        print(f"Weighted score = {weighted_1} / {midterm1_weight}")
        print()
        
    # Get midterm 2 information
    midterm2_weight = get_weight("Midterm 2:")
    midterm2_score = get_score("Midterm 2")
    midterm2_shifted = get_shift()
    if midterm2_shifted == 1:
        midterm2_score += get_shift_amount()
        midterm2_score = min(100, midterm2_score)
        print(f"Total points = {midterm2_score} / 100")
        weighted_2 = round((midterm2_score / 100)*(midterm2_weight), 1)
        print(f"Weighted score = {weighted_2} / {midterm2_weight}")
        print()
    else:
        print(f"Total points = {midterm2_score} / 100")
        weighted_2 = round((midterm2_score / 100)*(midterm2_weight), 1)
        print(f"Weighted score = {weighted_2} / {midterm2_weight}")
        print()

    # Get final exam information
    final_weight = get_weight("Final:")
    final_score = get_score("Final")
    final_shifted = get_shift()
    if final_shifted == 1:
        final_score += get_shift_amount()
        final_score = min(100, final_score)
        print(f"Total points = {final_score} / 100")
        weighted_final = round((final_score / 100)*(final_weight), 1)
        print(f"Weighted score = {weighted_final} / {final_weight}")
        print()
    else:
        print(f"Total points = {final_score} / 100")
        weighted_final = round((final_score / 100)*(final_weight), 1)
        print(f"Weighted score = {weighted_final} / {final_weight}")
        print()
    

    # Get homework information
    homework_weight = get_weight("Homework:")
    num_assignments = int(input("Number of assignments? "))
    homework_total_score = 0
    homework_total_max = 0
    for i in range(1, num_assignments + 1):
        assignment_score = int(input(f"Assignment {i} score? "))
        assignment_max = int(input(f"Assignment {i} max? "))
        homework_total_score += assignment_score
        homework_total_max += assignment_max
    section_attendance = int(input("How many sections did you attend? "))
    section_points = min(section_attendance * 3, 34)
    print(f"Section points = {section_points} / 34")
    homework_total_score += section_points
    print(f"Total points = {homework_total_score} / {homework_total_max+34}")
    homework_weighted = round(((homework_total_score) / (homework_total_max+34))*homework_weight,1)
    print(f"Weighted score = {homework_weighted} / {homework_weight}")
    print()

    
    # Calculate overall percentage
    overall_percentage = round((weighted_1 + weighted_2 + weighted_final + homework_weighted), 1)

    # Print overall percentage and minimum grade
    print(f"Overall percentage = {overall_percentage}")
    print("Your grade will be at least: ", get_minimum_grade(overall_percentage))

# Weights 
def get_weight(category):
    print(category)
    return int(input("Weight (0-100)? "))

# Get the score 
def get_score(category):
    return int(input("Score earned? "))

# check the shift
def get_shift():
    return int(input("Were scores shifted (1=yes, 2=no)? "))

# Get shift amount
def get_shift_amount():
    """Gets the amount of the shift in scores from the user."""
    return int(input("Shift amount? "))

# Get the grade report 
def get_minimum_grade(grade):
    
    if grade >= 90:
        return "A"
    elif 80 <= grade <= 89.99:
        return "B"
    elif 70 <= grade <= 79.99:
        return "C"
    elif 60 <= grade <= 69.99:
        return "D"
    else:
        return "F"
        
    
# Call the main function
if __name__ == "__main__":
    main()
