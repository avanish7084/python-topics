"""
def fun1():
    print("hello")

fun2=fun1
del fun1 # shallow copy
fun2()
"""

"""
#return  function  by functions
def fun(num ):
    if num==0:
        return  print
    if num==1:
        return sum
print(fun(1))
"""

"""
# as parametar function
def excute(fun1):
    fun1("this")

excute(print)

"""



#############  concept of decorators ###############

def dec1(fun1):
    def nowexecute():
        print("Executing now")
        fun1()
        print("Executed")
    return nowexecute
@dec1  #
def fun1():
    print("Hello")

#aa=dec1(fun1) === @dec1
fun1()




