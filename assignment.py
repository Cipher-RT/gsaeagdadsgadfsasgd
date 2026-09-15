# You can remove 'pass' if you written code in the function
# Exercise 1

def find_all_positions(data, target):
    #def linear_search(data, target):
    a=[]
    for i in range(len(data)):
        if data[i] == target:
            a.append(i)
    return a
    pass


# Exercise 2
def find_student_by_id(records, student_id):
    # Write your code here
    for student in records:
        if student[0]==student_id:
            return student[1]
    return
    pass

# Exercise 3
def binary_search_steps(data, target):
    # Write your code here
    pass

# Exercise 4
def find_insert_position(data, value):
    # Write your code here
    pass

# Exercise 5
def first_and_last_position(data, target):
    # Write your code here
    pass
