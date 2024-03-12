
#1
l = [2]
print(eval('*'.join(map(str,l))))
#2
str = input()
low=list(filter(lambda x: x.isupper(),str))
up=list(filter(lambda x: x.islower(),str))
print(len(low),len(up))
#3

str1 = input()
rstr = ''.join(reversed(str1))
if str1.lower() == rstr.lower():
    print('yes')
else:
    print('no')

#4
import time
a=float(input("Sample input:\n"))
t=float(input())
time.sleep(t/1000)
print(f'Sample output:\nSquare root of {a} after {t} milliseconds is {a**0.5}')
#5
print(all(list))



