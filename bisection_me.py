import math

func = str(input("Enter the function : "))
func = "lambda x : " + func
f = eval(func)

def getInitialRange():
    a = float(input("Enter the lower range : "))
    b = float(input("Enter the upper range : "))

    return a,b



def bisection(e,a,b):

    while(True):
        temp = (a + b) /2

        if( f(temp) < 0 ):
            a = temp
            print("a : ",a," b : ",b," f(x) : ",f(temp))
            if(abs(f(temp)) < e):
                return temp
        else:
            b = temp
            print("a : ",a," b : ",b," f(x) : ",f(temp))
            if(abs(f(temp)) < e):
                return temp
    

    


a,b = getInitialRange()
e = float(input("Error : "))
sol = bisection(e,a,b)
print("Solution : ",sol)
