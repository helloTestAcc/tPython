#DemoFormat.py
# strUrl="www.credu.com/?page="+1
# print(strUrl)

strURL="www.credu.com/?page=" + str(1)
print(strURL)


for x in range(1,6):
    print(x,"*", x, "=",x*x)


print("정렬지정")

for x in range(1,6):
    print(x,"*", x,"=", str(x*x).rjust(3))
