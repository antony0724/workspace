#!/usr/bin/env python
# coding: utf-8

# In[23]:


fruits = ['蘋果','香蕉','櫻桃','芒果','榴槤','鳳梨','柚子','芭樂','梨子','木瓜']
print('----1----')
print(fruits)
print('----2----')
print(fruits[4])
print('----3----')
print(fruits[-1])
print('----4----')
print(fruits[2:6])
print('----5----')
PickFruit=fruits.pop(2)
print(PickFruit)
print(fruits)
print('----6----')
fruits.insert(1,'蜜桃')
print(fruits)
print('----7----')
fruits.append('非洲甜橙')
print(fruits)
country = ['亞洲','非洲','美洲']
print('----8----')
print(country)
print('----9----')
fruits.extend(country)
print(fruits)


# In[ ]:




