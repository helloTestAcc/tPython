#demoTuple, set.py
#set  순서없고 유니크한 집합
a={1,2,3,3,3}
b={2,3,4,5,3}

print(a)
print(b)

print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


#  tuple은 입력된 순서대로 출력(read only)
print("tuple")

tp = (1,2,3)

print(type(tp))

print(tp.count)
print(tp.index(2))


#함수정의

print("함수")

def calc(a,b):
    return a+b, a*b

#호출

result=calc(3,4)
result=calc(1,2)
print(result)

# 형식 변환

a=set((1,2,3))
print(a)
print(type(a))


b= list(a)
b.append(4)

print(type(b))

print(b)


print("----------dict")
color={"apple":"red", "banana":"yellow"}
print(color["apple"])
print(len(color))
#입력
color["kiwi"]="green"
print(len(color))
#삭제
del color["apple"]
print(color)




phone={"kim":"010-1010-0101", "lee":"010-2020-2020","park":"010-3030-3030"}

#print( phone[0] )
for item in phone.items():
    print(item)

for a,b in phone.items():
    print(a,b)


print("park" in phone)
print("kang" not in phone)

p=phone
print(p)

print(id(phone), id(p))