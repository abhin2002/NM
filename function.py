
func = str(input("Enter the function : "))
func = "lambda x : " + func
f = eval(func)
print(f(2))