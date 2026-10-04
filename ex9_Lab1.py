import pandas as pd
courses = {}
while True:
    course = input("Course (done to finish): ")
    if course == "done":
        break
    grade = float(input("Grade: "))
    courses[course] = grade
    pd.DataFrame(courses.items(), columns=['Course', 'Grade']).to_csv('grades.csv', index=False)
    print(pd.Series(courses).describe())
                                                                
                                                                      