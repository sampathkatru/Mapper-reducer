text = open("input.txt", "r")
li=[]
data=text.read()
d=data.split()
li.append(d)
print(li)
mapper = open("mapper.txt", "a")
for x in li:
    for y in x:
      it=str(y).lower()
      print(it+' 1')
      mapper.write(it+' 1\n')
mapper.close()
