import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table if not exists PhoneBook (id integer primary key autoincrement, name text, phoneNum text);")
cur.execute("insert into PhoneBook(name, phoneNum) values ('홍길동', '010-0101-0110');")

cur.execute("select * from PhoneBook")
print(dir(cur))
for row in cur:
    print(dir(row))
    print(row)

# 외부에서 입력 파라미터 받기

name='이순신'
phoneNumber='0101-1011--1111'
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);",(name, phoneNumber))

cur.execute("select * from PhoneBook")
print(dir(cur))
for row in cur:
    print(dir(row))
    print(row)
    print("{0}, {1}, {2}".format(row[0], row[1], row[2]))


# 다중행 입력
datalist=(("tom", "0101-110012"), ("dsp","010-30003-"))

cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",(datalist))

cur.execute("select * from PhoneBook ")
print(dir(cur))
for row in cur:
    print(row)
    print("{0}, {1}, {2}".format(row[0], row[1], row[2]))
