#strtest.py

#dir(str)
#print(dir(str))

print((str(dir(str))))

u=" spam and ham "
#str preprocessing
u.strip()
print(u.strip())
u.rstrip()
print(u.rstrip())
u.lstrip()
print(u.lstrip())
print('test'.join(u.split('a')))
#(dir(str)).capitalize("capitalize")

#demo code

print("\n".join(str(dir(str)).split('\'')))

#pirnt(dir(str)))


strA="python is very powerful"
strB="파이썬은 강력해"

print(len(strA))

print(len(strB))

print(strA.capitalize()) #대문자 첫
print(strA.count("p")) # 카운팅
print(strA.count("p",7)) # 7글자 이후

print(strA.startswith("python")) # 패턴 체크
print(strA.endswith("ful"))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

#
print("문자열 공백제거")
t="<<< spam and hma >>>"
print(t)
result=t.strip()
print(t.strip())
print(t)
print(result)
result=t.strip("<")
result=t.strip(">")
result=t.strip("<> ")
print(result)
result=t.replace(" ","").strip("<>")
print(result)

result2=t.replace("spam", "spam egg")
print(result2)
lst=result2.split()
print(lst)
lst.remove("egg")
print("------------------")
print(":)".join(lst))