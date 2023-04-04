# 전역변수

str = "Not Class Member"
class GString:
    def __init__(self):
        #instance 멤버변수        
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)


#인스턴스 생성
g = GString()
g.set("First Message")
g.print()

class k:
    def __str__(self,t):
        return "메롱"+t
    

kk = k()
print(kk.__str__("a"))
