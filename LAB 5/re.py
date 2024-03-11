#1
import re
with open('row.txt') as file:
    lines=file.readlines()
for i in lines:
    if(re.findall("a(b*)",i)):
        print(i)

#2
for i in lines:
    if(re.findall("ab{2,3}[^b].*",i)):
        print(i)

#3
for i in lines:
    if(re.findall("[a-z]_[a-z]",i)):
        print(i)

#4
for i in lines:
    if(re.findall("[A-Z][a-z]",i)):
        print(i)

#5
for i in lines:
    if(re.findall("^a.*b$",i)):
        print(i)

#6
for i in lines:
    print(re.sub(r"[ .,]",":",i))

#7
for i in lines:
    print(re.sub("_[a-z]",lambda a:a.group(0).upper()[1::],i))

#8
for i in lines:
    print(re.split("[A-Z]",i))

#9
for i in lines:
    print(re.sub(r"(\w)([A-Z])",r"\1 \2",i))

#10
i="AbcAbcsdAbcsdf"
print(re.sub(".[A-Z]",lambda a: f'{a.group().lower()[0]}_{a.group().lower()[1]}',i))