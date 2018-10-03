
# coding: utf-8

# In[1]:


book= ['英文','數學','財務','工程','國文','地理','歷史','生物','地科','公民','微積分','物理','化學','國防','線性代數']
print(1)
print(book)

print(2)
print(book[7])

print(3)
print(book[0],book[14])

print(4)
print(book[9:12])

sbook=list()
sbook1=book.pop(14)
sbook2=book.pop(13)
sbook=sbook1+' '+sbook2
print(5)
print(sbook)
print(book)

book.insert(4,'作業研究')
print(6)
print(book)

country=['韓國','日本','台灣','美國','新加坡']
print(7)
print(country)

book.extend(country)
print(8)
print(book)

