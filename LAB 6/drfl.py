import os
#1
path = "C:\Users\Asus\Documents\LABS\LAB 6"
dirs = os.listdir(path)
print(f'folders and files in path - "{path}":\n', dirs)

#2
path="C:\Users\Asus\Documents\LABS\LAB 6"
print('Exists:', os.access(path, os.F_OK))
print('Access to read:', os.access(path, os.R_OK))
print('Access to write:', os.access(path, os.W_OK))
print('Can be executed:', os.access(path, os.X_OK))

#3
path = "C:\Users\Asus\Documents\LABS\LAB 6\builtin.py"
if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path does not exist')

#4
with open('Sample.txt','r') as file:
    lines=file.readlines()
print('lines:',len(lines))

#5
list=list(input().split())
with open('Void.txt','w') as file:
    for i in list:
        file.write(str(i))

#6
import string
for letter in string.ascii_uppercase:
    with open(f'{letter}.txt', 'w'):
        pass

#7
with open('Sample.txt', 'r') as file:
    data = file.read()
with open(r'Copy.txt', 'w') as file:
    file.write(data)

#8
with open('Deleted.txt', 'w') as file:
    pass
path = '"C:\Users\Asus\Documents\LABS\LAB 6\Deleted.txt"'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.W_OK):
        print(f'File "{name}" can be accessed')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be accessed')
else:
    print(f'File "{name}" does\'t exist')