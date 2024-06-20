#Grade statistics exercise
#Step 1 - Get exam and exercise results from users
def main():
    exam_points = []
    exercises = []
    exercise_points = []
    total_points = []

    exam_and_exercise = input("Exam and exercises completed: ")
    while True:    
        if exam_and_exercise != "":
            points_list = exam_and_exercise.split()
            exam_points.append(points_list[0])
            exercises.append(points_list[1])
            exam_and_exercise = input("Exam and exercises completed: ")
        else:
            exam_points = [int(point) for point in exam_points] #conver to int
            exercises = [int(exercise) for exercise in exercises] #convert both to int
            #get exercise points
            for i in exercises:
                exercise_points.append(i//10) 
            #get total points 
            for i in range(len(exercises)):
                total_points.append(exam_points[i] + exercise_points[i])   
            break 
        #now we have exam_points, exercise_points and exercises saved as identically long lsits

    #Step 2 - Set up grading system

    #def grade(exam_points, total_points):

    fail = ""
    grade1 = ""
    grade2 = ""
    grade3 = ""
    grade4 = ""
    grade5 = ""

    for i in range(len(total_points)):
        if exam_points[i] < 10 or total_points[i] >= 0 and total_points[i] <= 14:
            fail += "*"
        elif total_points[i] >= 15 and total_points[i] <= 17:
                grade1 += "*"
        elif total_points[i] >= 18 and total_points[i] <= 20:
                grade2 += "*"
        elif total_points[i] >= 21 and total_points[i] <= 23:
                grade3 += "*"
        elif total_points[i] >= 24 and total_points[i] <= 27:
                grade4 += "*"
        elif total_points[i] >= 28 and total_points[i] <= 30:
                grade5 += "*"

    all_grades = grade1+grade2+grade3+grade4+grade5+fail
    passing_grades = grade1+grade2+grade3+grade4+grade5
    pass_percentage = passing_grades.count("*")/all_grades.count("*")*100

    # Round the pass percentage and points average to two decimal places
    points_average = round(sum(total_points) / len(total_points), 1)
    pass_percentage = round(pass_percentage, 1)

    print("Statistics:")
    print(f"Points average: {points_average}")
    print(f"Pass percentage: {pass_percentage}")
    print(f"Grade distribution:")
    print(f"5: {grade5}")
    print(f"4: {grade4}")
    print(f"3: {grade3}")
    print(f"2: {grade2}")
    print(f"1: {grade1}")
    print(f"0: {fail}")
    
if __name__ == "__main__":
    main()