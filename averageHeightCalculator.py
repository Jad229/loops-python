# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
amt = 0

print(student_heights)
for height in student_heights:
    amt += 1
    sum += height
   
average_height = round(sum/amt)

print(average_height)

