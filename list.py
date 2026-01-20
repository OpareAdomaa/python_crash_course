courses = ['Statistics', 'Numerical analysis', 'MicroP', 'Data structures and Algorithms'] # list of courses
print(courses[3], courses[2], courses[1]) # printing last three courses
print(f'One of my courses this sem is {courses[-1]}') # using f-string to print last course
courses.append('Python') # adding a new course
courses.sort() # sorting the list of courses
print(courses) # sorting the list of courses

for course in courses:
    print(course)   
