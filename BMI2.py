import time
a = time.time()
name =[('林姍'),('王志祥'),('李明立'),('黃婷婷'),
('張文智'),('陳怡君'),('王凱群'),('林曉曉')]
height = [155,175,172,162,180,158,170,156]
weight = [45,85,68,52,72,48,80,70]

student = []
for i in range(len(name)):
  student.append([])
  student[i].append(name[i])
  student[i].append(height[i])
  student[i].append(weight[i])
print(student)

print('請平日進行飲食的調整，以維持健康的身體')
print('姓名',' ','BMI')
for i in range(len(student)):
    BMI=student[i][2]/((student[i][1]/100)**2)
    if BMI>=27:
        print(student[i][0],BMI)
b = time.time()
print (b-a)