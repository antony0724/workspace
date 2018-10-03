
# coding: utf-8

# In[6]:


people=[('林威豪','台北市'),('黃安安','高雄市'),('林湘琦','台中市'),('陳遠見','台南市'),('林萊萱','台中市'),('許志祥','台北市'),
        ('呂姍姍','嘉義市'),('張柏凱','桃園市')]
newpeople=[('林威豪','台北市'),('黃安安','高雄市'),('林湘琦','台中市'),('陳遠見','台南市'),('林萊萱','台中市'),('許志祥','台北市'),
        ('呂姍姍','嘉義市'),('張柏凱','桃園市')]
pick=list()

for i in range(0,len(people)):
    print(people[i][0],people[i][1]) 
print("*********************")
for j in range(0,len(people)):
    if (people[j][1] == '台北市'):
        del newpeople[j]
        pick.append(people[j])
for k in range(0,len(pick)):
    print(pick[k][0],pick[k][1])
print("*********************")
for m in range(0,len(newpeople)):
  print("第",m+1,"位同學",newpeople[m][0],":家住",newpeople[m][1]);

