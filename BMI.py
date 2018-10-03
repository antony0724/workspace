#!/usr/bin/env python
# coding: utf-8

# In[49]:


student = [('林姍',155,45),('王志祥',175,85),('李明立',172,68),('黃婷婷',162,52),
           ('張文智',180,72),('陳怡君',158,48),('王凱群',170,80),('林曉曉',156,70)]
print('請平日進行飲食的調整，以維持健康的身體')
print('姓名',' ','BMI')
for i in range(len(student)):
    BMI=student[i][2]/((student[i][1]/100)**2)
    if BMI>=27:
        print(student[i][0],BMI)

    



# In[ ]:




