class ControlStructures:
    def num(self):
        n=int(input())
        result=""
        if(n%2==0):
            print("num is even")
            result="even"
        else:
            result="odd"
            print("num is odd")
            return result
m=ControlStructures().num()
print(m)