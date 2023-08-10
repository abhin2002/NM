import math

func = str(input("Enter the function : "))
func = "lambda x : " + func
f = eval(func)

def getInitialRange():
    a = float(input("Enter the lower range : "))
    b = float(input("Enter the upper range : "))

    return a,b

def falsePosition(a,b,e):

    while(True):
        temp = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))

        if( f(temp) < 0):
            a = temp
        else:
            b = temp
        
        print("a : ",a," b : "," f(x) : ",f(temp))
        if(abs(f(temp)) < e):
            return temp


a,b = getInitialRange()
e = float(input("Enthe the error : "))
sol = falsePosition(a,b,e)
print("Solution : ",sol)
