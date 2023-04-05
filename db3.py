#db3.py

#db2.py
import sqlite3
from os.path import *
con = sqlite3.connect(":memory:")
#con=sqlite3.connect("c:\\work\\sample.db")


cur = con.cursor()
cur.execute("create table if not exists PhoneBook (id integer primary key autoincrement, name text, phoneNum text);")
cur.execute("insert into PhoneBook(name, phoneNum) values ('홍길동', '010-0101-0110');")

cur.execute("select * from PhoneBook")

# 외부에서 입력 파라미터 받기

name='이순신'
phoneNumber='0101-1011--1111'
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);",(name, phoneNumber))

cur.execute("select * from PhoneBook")

# 다중행 입력
datalist=(("tom", "0101-110012"), ("dsp","010-30003-"))

cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",(datalist))

cur.execute("select * from PhoneBook ")

print("fetchone")
print(cur.fetchone())
print("fetchmany(2)")
print(cur.fetchmany(2))
print("fetchall")
print(cur.fetchall())


#쓰기(insert delete update => 커밋 필요)

con.commit()