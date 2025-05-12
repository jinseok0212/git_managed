'''a = [1, 2, 3]

print(a)
print(a[0] + a[2])

b = [1, 2, 3, a]

print(b[3][2])

print(b[0:2]) #리스트 

dic = {'name' : 'jinseok', 'phone' : '01024688483', 'birth' : '0212'}


print(dic['birth'])

print(bool([])) 
B = 1
def a(B):
    B = B +1
    return B
print(a(B)) # 함수 
print(B)

a = int(input("number : "))
print(type(a)) '''


class cal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second


class more(cal):
    def pow(self):
        return self.first ** self.second




if __name__ == "__main__":

    a = more(4, 2)
    b = more(4,7)
    print(a.pow(), b.pow())

    class family:
        lastname = '최'

    a.family()
    a.lastname = '박'