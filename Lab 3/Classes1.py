N1
class Upper:
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("string: ")
    def printString(self):
        print(self.s.upper())
x=Upper()
x.getString()
x.printString()

N2
class Shape:
    def area(self):
        self.a=0
        print("area:",self.a)
class Square(Shape):
    def __init__(self):
        self.length=int(input("length: "))
    def area(self):
        self.a=self.length*self.length
        print("area:",self.a)
x=Square()
x.area()

N3
class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("length: "))
        self.width=int(input("width: "))
    def area(self):
        self.a=self.length*self.width
        print("area: ",self.a)
x=Rectangle()
x.area()

N4
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"point: {self.x}, {self.y}")
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
        print(f"new point: {self.x} , {self.y}")
    def dist(self):
        x2, y2 = int(input("2nd point x: ")), int(input("2nd point y: "))
        distance = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        print("distance:",distance)


x1, x2 = int(input("x: ")), int(input("y: "))
result = Point(x1, x2)
result.show()
nx, ny = int(input("new x: ")), int(input("new y: "))
result.move(nx, ny)
result.dist()

N5
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,d):
        self.d = d
        self.balance += self.d
        print("balance:", self.balance)
    def withdraw(self,w):
        self.w = w
        p = True
        self.balance -= self.w
        if self.balance < 0:
            p = False
            self.balance += self.w
            print("no money withdraw")
        print("balance:",self.balance)
owner = input("owner: ")
balance = int(input("balance: "))
x = Account(owner, balance)
x.deposit(int(input("deposit: ")))
x.withdraw(int(input("withdraw: ")))
x.deposit(int(input("deposit: ")))
x.withdraw(int(input("withdraw: ")))
x.deposit(int(input("deposit: ")))
x.withdraw(int(input("withdraw: ")))

N6
nums = list(map(int,input().split()))
def prime(x):
    if x==1:
        return False
    else:
        for i in range(2, x):
            if x%i==0:
                return False
        return True
print(list(filter(prime,nums)))