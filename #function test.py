#function test.py

#1)  함수를 정의

def setValue(newValue):
    x=newValue
    print("내부: ", x)
    return x




#2) 함수를 호출

retValue = setValue(5)

print(type(
    retValue))

print(__file__)

def swap(x,y):
    return y,x

# 호출

retVlue = swap(3,5)

print(retValue)






#디버깅을 위한 함수(교집합)

def intersect(prelist, postlist):
    #지역변수로 리스트에 글자를 모아두기
    result=[]

    #H(0) | A(1) | M(2)
    for x in prelist:
        # 어떤 글자가  postlist에 있고  x가  result에 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM", "SPAM"))


def swap(x,y):
    return (y,x)
retValue=swap(4,5)
print(retValue)
print(retValue[0], retValue[1])



x=1

def func(y):
   # x=x+1
    return x+y
print(x)
print(func(1))
print(x)

g= lambda x,y:x+y
print(g(2,3))
(lambda x:x*x(3))

print(g(3,3))
