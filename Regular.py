#Regular.py

#\b 질문 하는게 좋은지 전처리하는게 좋은지


import re

result = re.search("[0-9]*th", "  35th")

print(result)
print(result.group())


# #매치는 공백때문에 못찾음. 널에러(논에러)
# result = re.match("[0-9]*th", "35th")#result = re.match("[0-9]*th", "  35th")

# print(result)
# print(result.group())


result = re.search("ap", "This is Apple".lower())
print(result.group())


# result=re.match("ap", "This is apple")
# print(result.group())#


result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
result = re.search("\d{4}", "우리동네는 52300입니다..")
print(result.group()) #질문 \d4일경우 5230이 나오는데 에러가 나오게 하려면?

#크몽n잡러

#라인넘버=>변수줘서
