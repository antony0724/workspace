allname=[]
allword=[]
allhour=[]

while True:
  name,words,hours=input("請輸入姓名,字數/小時,時數").split(',')
  stop=input("不在輸入請按n,繼續請按y")
  words=int(words)
  hours=int(hours)
  allname.append(name)
  allword.append(words)
  allhour.append(hours)
  
  if stop=='n':
    break


allmoney=list(map(lambda a,b:((a/200)*10)*b,allword,allhour))
print('姓名',' ','薪水')
for i in range(len(allname)):
  print(allname[i],allmoney[i])