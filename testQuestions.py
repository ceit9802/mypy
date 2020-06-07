def q1():
    print(2 ** 3 ** 2 ** 1)

def q2():
    print("Peter's sister's name's \"Anna\"")
    print('Peter\'s sister\'s name\'s \"Anna\"')

def q3():
    i = 250 
    while len(str(i)) > 72: 
        i *= 2 
    else: 
        i //= 2 
    print(i)


def q4():
    n = 0 
    while n < 4: 
        n += 1
        print(n, end=",")

def q5():
    x = 0 
    y = 2 
    z = len("Python") 
    x = y > z 
    print(x)

def q6():
    Val = 4 
    Val2 = 0 
    Val = Val ^ Val2 
    print(Val)
    Val2 = Val ^ Val2 
    print(Val2)
    Val = Val ^ Val2    
    print(Val)
def bitwise():
    x=7
    y=6
    print("x=",x," y=",y)
    print("~x=",~x)
    print("x^y=",x^y)
    print("x&y=",x&y)
    print("x|y=",x|y)
    print("x>>1=",x>>1)
    print("x<<1=",x<<1)
    print("x>>y=",x>>y)
    print("x<<y=",x<<y)


def q7():
    z, y, x = 2, 1, 0 
    x, z = z, y  #x=2,y=1,z=1
    y = y - z  #x=2,y=0,z=1
    x,y,z=y,z,x
    print(x, y, z)

def q8():
    a = 0 
    b = a ** 0  #any number raised to 0 is 1, so b=1
    if b < a + 1: 
        c = 1 
    elif b == 1: 
        c = 2 
    else: c = 3 
    print(a + b + c)

def q9():
    i = 10 
    while i > 0 : 
        i -= 3 
        print("*") 
        if i <= 3: 
            break 
    else: print("*")

def q10():
    print('# Example 1')
    for i in range(1, 4, 2): 
        print("*") 
    print('# Example 2') 
    for i in range(1, 4, 2): 
        print("*", end="")
    print('# Example 3') 
    for i in range(1, 4, 2): 
        print("*", end="**") 
    print('# Example 4') 
    for i in range(1, 4, 2): 
        print("*", end="**") 
    print("***")

def q12():
    x = "20" 
    y = "30" 
    print(x > y)

def q13():
    s="Hello, Python!"
    print(s[-14:1])
    print(s[-14:])
    print(s[-14:15])

def q14():
    lst = ["A", "B", "C", 2, 4] 
    del lst[0:2] 
    print(lst)

def q15():
    dict = { 'a': 1, 'b': 2, 'c': 3 } 
    for item in dict: 
        print(item)

def q16():
    s = 'python' 
    for i in range(len(s)): 
        i = s[i].upper() 
    print(s, end="")

def q17():
    lst = [i // i-3 for i in range(1,4)] 
    print(lst)
    sum = 0 
    for n in lst: 
        sum += n 
    print(sum)

q17()