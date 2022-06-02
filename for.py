#counting letters in a string
str="Hello guys welcome back"
count=0.
for x in str:
    if x!='l':
      print(x)
outstr="Hello guys welcome back"
count=0.
for x in str:
    if x!='l':
      outstr +=x
print(outstr)
outstr="Hello guys welcome back"
count=0.
for x in str:
    if x!='e':
      outstr +=x
print(outstr)