
# x = eval(input("Ente the value for x : "))
# y = eval(input("Enter the value for y : "))
# k = eval(input("Enter the value for k : "))

x = [45, 50, 55, 60, 65]
y = [114.84, 96.16,83.22,74.48,68.48]
k = 52

def leg(x,y,k):
    yk = 0
    for i in range(len(x)):
        temp = y[i]
        for j in range(len(x)):
            if(i != j):
                temp = temp * (k - x[j])
                temp = temp * (1/(x[i] - x[j]))
        yk += temp 
    print(yk)

leg(x,y,k)