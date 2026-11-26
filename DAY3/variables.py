print("Assigning multiple values to multiple variables:")
num1, num2, num3 = 10,20,30
print("number1 value:",num1)
print("number2 value:",num2)
print("number3 value:",num3)
print("All variables reference are:",id(num1), id(num2), id(num3))








print("-----------------------------------------------------------------------")
print("Assigning single values to multiple variables:")
num1,num2,num3=10,10,10
#num1=num2=num3=10
print("number1 value:",num1)
print("number2 value:",num2)
print("number3 value:",num3)
print("All variables reference are:",id(num1), id(num2), id(num3))



print("-----------------------------------------------------------------------")

print("if the value was execeeding the limit then the id will be:")
num1,num2,num3=350,350,350
#num1=num2=num3=10
print("number1 value:",num1)
print("number2 value:",num2)
print("number3 value:",num3)
print("All variables reference are:",id(num1), id(num2), id(num3))



print("-----------------------------------------------------------------------")

print("Swapping two numbers:")
a,b=10,20
print("before swapping:")
print(a,b,id(a),id(b))
a,b=b,a
print(a,b,id(a),id(b))
