def addition(a,b):
    sum=a+b
    print(sum)
def subtract(a,b):
    sub=a-b
    print(sub)
def divide(a,b):
    try:
        div=a/b
        return div
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
def multiply(a,b):
    mul=a*b
    print(mul)