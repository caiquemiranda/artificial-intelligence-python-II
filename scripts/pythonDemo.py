fun_list1 = []

for i in range(5):

    def fun1(e):
        
        return e+i
    
    fun_list1.append(fun1)

fun_list2 = []

for i in range(5):

    def fun2(e,iv=i):
         
        return e+iv
    
    fun_list2.append(fun2)

fun_list3 = [lambda e: e+i for i in range(5)]
fun_list4 = [lambda e,iv=i: e+iv for i in range(5)]

i=56

# in Shell do
## ipython -i pythonDemo.py
# Try these (copy text after the comment symbol and paste in the Python prompt):
# print([f(10) for f in fun_list1])
# print([f(10) for f in fun_list2])
# print([f(10) for f in fun_list3])
# print([f(10) for f in fun_list4])

def myrange(start, stop, step=1):
    """enumerates the values from start in steps of size step that are
    less than stop. 
    """

    assert step>0, "only positive steps implemented in myrange"
    i = start
    
    while i<stop:
        yield i
        i += step

print("list(myrange(2,30,3)):",list(myrange(2,30,3)))

def ga(n):
    """generates square of even nonnegative integers less than n"""

    for e in range(n):
        if e%2==0:
            yield e*e
    
a = ga(20)

def myenumerate(enum):
    for i in range(len(enum)):
        yield i,enum[i]