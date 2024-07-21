file=open('mapper.txt','r')
li=[]
for i in range(1,99):
   freq=0
   data=file.readline()
   word=data.split()
   if '/' in data:
      break
   li.append(word)
lis=[item for sublist in li for item in sublist]
for i in lis:
   if '1' == i:
      lis.remove(i)
print(lis)
W=list(set(lis))
mapper = open("output.txt", "a")
for item in W:
   fr=0
   for freq in lis:
      if item==freq:
         fr+=1
   mapper.write(item+' '+str(fr)+'\n')