#WAP to convert celsius into farenheit scale


def fun(c):
    f=(9*c/5)+32
    return f
c=int(input("Enter the temperature in celsius "))

print(c,"°C is ",round(fun(c),2),'in F')

    