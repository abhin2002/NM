
import math

func = str(input("Enter the function : "))
func_deri = str(input("Enter the derivative of the function : "))
func = "lambda x : " + func
func_deri = "lambda x : " + func_deri
f = eval(func)
f_ = eval(func_deri)

def getInitialRange():
    a = float(input("Enter the lower range : "))
    b = float(input("Enter the upper range : "))

    return a,b

def newton(a,b,e):

    while(True):
        temp = b - (f(b) / f_(b))
        b = temp
        print("a : ",a," b : ",b," f(x) : ",f(temp))
        if(abs(f(temp)) < e):
            return temp

a,b = getInitialRange()
e = float(input("Enter the error : "))
sol = newton(a,b,e)
print("Solution : ",sol)


