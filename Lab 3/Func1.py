N1
def ounce(grams):
    print("ounces =",grams*28.3495231)
ounce(float(input("grams: ")))

N2
def celcius(fahrenheit):
    print("celcius =",(5/9)*(fahrenheit-32))
celcius(int(input("fahrenheit: ")))

N3
def solve(numheads, numlegs):
    print("rabbits =",int((numlegs-numheads-numheads)/2))
    print("chickens =",int(numheads-(numlegs - numheads - numheads)/2))
numheads = int(input("numheads: "))
numlegs = int(input("numlegs: "))
solve(numheads, numlegs)

N4
def filter_prime(n):
    a=0
    for i in range(1,n+1):
            if n%i==0:
                a=a+1
    return a==2
b=[x for x in map(int,input("list: ").split()) if filter_prime(x)]
print("primes:",b)

N5
from itertools import permutations
def permutate(st):
    p=permutations(st)
    for i in p:
        print(i)
permutate(input("string: "))

N6
def reverse(st):
    for i in range(len(st)):
        print(st[len(st)-i-1])
reverse(list(map(str, input("string: ").split())))

N7
def has_33(n):
    st=""
    for i in range(len(n)):
        st+=str(n[i])
        if(st.count("33")>=1):
            return "True"
    return "False"
print(has_33(list(map(int,input("numbers: ").split()))))

N8
def spy_game(n):
    st=""
    for i in range(len(n)):
        st+=str(n[i])
        if(st.count("007")>=1):
            return "True"
    return "False"
print(spy_game(list(map(int,input("numbers: ").split()))))

N9
import math
def volume(radius):
    return 4*math.pi*pow(radius,3)/3
print(volume(float(input("radius: "))))

N10
def unique(u):
    u.sort()
    for i in range(len(u)-1,0,-1):
        if(u[i]==u[i-1]):
            u.remove(l[i])
    print(u)
unique(list(input("list: ").split()))

N11
def pal(s):
    return s==s[::-1]
print(pal(input("phrase: ")))

N12
def histogram(h):
    for i in range(len(h)):
        print("*"*h[i])
histogram(list(map(int,input("list: ").split())))

N13
import random
def guess(s):
    r=random.randint(1,20)
    print(f"\nWell, {s}, I am thinking of a number between 1 and 20.")
    b=False
    i=0
    while(b==False):
        i+=1
        n=int(input("Take a guess\n"))
        if(r==n):
            print(f"\nGood job, {s}! You guessed my number in {i} guesses!")
            b=True
        elif(r>n):
            print("\nYour guess is too low.")
        else:
            print("\nYour guess is too high.")
guess(input("Hello! What is your name? \n"))