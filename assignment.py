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
    answer=[-1,0]
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            answer[0]=mid
            answer[1]+=1
            return answer  # found
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        answer[1]=answer[1]+1
    return answer
    pass
# Exercise 4
def find_insert_position(data, value):
    for i in range(len(data)):
        if data[i] >= value:
            return i
    return len(data)

# Exercise 5
def first_and_last_position(data, target):
    # Write your code here
    answer=[-1,-1]
    first=True
    for i in range(len(data)):
        value=data[i]
        if value==target:
            if answer[0]==answer[1] and first:
                answer[0]=i
                answer[1]=i
                first=False
            elif answer[0]<=answer[1] and not first:
                answer[1]=i
    return answer
