import random

print(random.random())
print(random.random())
print(random.uniform(1.0, 5.0))
print("--------randrange------")

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print("---------sample()---")
print(random.sample(range(20),10))
print(random.sample(range(20),10))

lotto = list(range(1,46))
print(lotto)
print(random.shuffle(lotto))
print(lotto[:6])
print(random.shuffle(lotto))
print(lotto[:6])


from os.path import *

print("파일정보")
print(abspath("python.exe")) #절대경로
print(basename("c:\\python310\\python.exe"))#파일이름
print("파일이있음:{0}".format(exists("c:\\python310\\python.exe")))

print(getsize("c:\\python310\\python.exe"))

print(dir())
print(dir())

#os정보
import os
print("os이름:{0}".format(os.name))
#os.system("notepad.exe")
print(dir(os.path))

import glob
print("현재폴더:{0}".format(os.getcwd()))
os.chdir("..")
os.chdir("c:\\work")
result = glob.glob("*.txt") #특정폴더 내 특정파일 걸르기
print(result)

for item in result:
    
    print(normpath(abspath(item)))
    #print(basename(item))

os.system('c:\work\results.txt')