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
    lst = [i //i for i in range(0,4)] 
    print(lst)
    sum = 0 
    for n in lst: 
        sum += n 
    print(sum)
def q18():
    lst = [[c for c in range(r)] for r in range(3)] 
    for x in lst: 
        for y in x: 
            if y < 2: 
                print('*', end='')
def q19():
    lst = [2 ** x for x in range(0, 11)] 
    print(lst[10])
    print(lst[-1])

def q20():
    lst1 = "12,34" 
    lst2 = lst1.split(',') 
    print(len(lst1) < len(lst2))

def funQ21(a, b=0, c=5, d=1): 
    return a ** b ** c
def q21():
    print(funQ21(b=2, a=2, c=3))    

def q22():
    x = 5 
    f = lambda x: 1 + 2 
    print(f(x))
def q23():
    from math import pi as xyz
    #print(pi)
    print(xyz)
def q25():
    from random import randint 
    for i in range(10): 
        #print(random(1, 5))
        print(i,' -- ', randint(1,5))

def q26():
    x = 1 
    def a(x):  
        return 2 * x 
    x = 2 + a(x) 
    print(a(x))


def q27():
    a='hello'    
    def q27x(a,b):
        z=a[0]
        return z
    #print(q27x(a))
    print(q27x(a,None))

def q28():
    s = 'SPAM' 
    def f(x): return s + 'MAPS' 
    print(f(s))

def q30():
    def gen(): 
        lst = range(5) 
        for i in lst: 
            yield i*i 
    for i in gen(): 
        print(i, end="")

def q34():
    def a():
        x = 1 
        y = 0 
        z = x%y 
        print(z) 
    def b():
        x = 1 
        y = 0 
        z = x/y 
        print(z)
    #a()
    b()
def q35():
    x = 0
    try: 
        print(x) 
        print(1 / x) 
    except ZeroDivisionError: 
        print("ERROR MESSAGE") 
    finally: 
        print(x + 1) 
    print(x + 2)
def q36():
    class A: 
        def a(self): 
            print("A", end='') 
    class B(A): 
        def a(self): 
            print("B", end='') 
    class C(B): 
        def b(self): 
            print("B", end='') 
    a = A() 
    b = B() 
    c = C() 
    
    a.a() 
    b.a() 
    c.b()

def q37():
    try: 
        print("Hello") 
        raise Exception 
        print(1/0) 
    except Exception as e: 
        print(e)
def q38():
    def q38a():
        class CriticalError(Exception): 
            def __init__(self, message='ERROR MESSAGE A'): 
                Exception.__init__(self, message) 
        raise CriticalError 
        raise CriticalError("ERROR MESSAGE B") 
    def q38b():
        class CriticalError(Exception): 
            def __init__(self, message='ERROR MESSAGE A'): 
                Exception.__init__(self, message)
        raise CriticalError("ERROR MESSAGE B")

    #q38a()
    q38b()

def q39():
    file = open('/home/ragingbull/work/mypy/helloPyWorld.py') 
    # insert code here 
    #print(file.readlines())
    #for l in file: print(l)
    #print(file.lines())
    print(file.read())
    file.close()

def q40():
    f = open("/home/ragingbull/work/mypy/helloPyWorld.py", "w") 
    f.close()

q40()