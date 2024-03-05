#1
def squares(n):
    num = 0
    while num <= n:
        yield num ** 2
        num += 1
#2
def even(n):
    num = 0
    while num <= n:
        if num%2 == 0:
            yield num
        num+=1
b = int(input())
list = []
for j in even(b):
    list.append(j)
print(list)
#3
def div(n):
    num = 0
    while num<=n:
        if num%3 == 0 or num%4 == 0:
            yield num
        num+=1
        
#4
def sqr(a,b):
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
for i in sqr(a,b):
    print(i)
   
#5
def rev(n):
    z = n 
    while z>=0:
        yield z
        z-=1
ab = int(input())
for i in rev(ab):
    print(i)
            
    
