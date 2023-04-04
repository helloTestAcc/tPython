#FORMAT.py


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))


#file write


f=open("c:\\work\\demo.txt", "wt", encoding="utf-8")

f.write("처음에는\n두번째라인\n세번째라인\n")
f.close()

#file open
# f=open("c:\\work\\demo.txt", "rt", encoding="utf-8")
# result=f.read()
# print(result)
# f.close()

#파일 읽기 새로운 작업

f=open("c:\\work\\demo.txt", "rt", encoding="utf-8")
result=f.read()
print(result)
print(f.tell())
# 다시 처음으로 파일포인터 이동
f.seek(0)
lst=f.readlines()
print(lst)

f.seek(0)
#코드로 보정
#print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())


print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")




f.close()
