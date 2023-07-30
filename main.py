# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# 156 178 165 171 187 156 178
# ask the heights of 7 people
# add all of them
# divide the result by 7
# round the answer to a whole number and print the result
total_sum = 0
total_students = 0
for student_height in student_heights:
    total_sum += int(student_height)
for amount in student_heights:
    total_students += 1
print(total_sum)
print(total_students)
average = round(total_sum/total_students)
print(average)



