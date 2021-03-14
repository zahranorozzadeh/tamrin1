import math
op=input()

if op=="sqrt" or op=="sin" op=="tan"  op=="cot"  op=="factoriel" op=="radians":
    a=float(input()) 
else:
a = float(input())
b = float(input())

if op == "+":
result = a+b

elif op == "-":
result = a-b

elif op == "*":
result = a*b

elif op == "/":
    if b == 0"
        result ="can not divid by zero"
    else:
        result = a/b
elif  op=="^"
    result= a**b   

elif  op=="log":
    result=math.log(a,b)  

elif  op="sqrt"
    result=math.sqrt(a) 

elif  op="sin"
    result=math.sin(a) 

elif  op="cos"
    result=math.cos(a)   


elif  op="tan"
    result=math.tan(a)     

elif  op="cot"
    result=1/math.tan(a)

elif  op="fatoriel"
    result=math.factorial(a)  

elif  op="radians"
    result=math.radians(a)              
              


else:
    result = "Error! operator not found!""

print(result)