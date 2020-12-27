from art import logo
print(logo)
def add(n1,n2):
    return(n1+n2)
def subtraction(n1,n2):
    return(n1-n2)
def multiply(n1,n2):
    return(n1*n2)
def divide(n1,n2):
    return(n1/n2)

operations={"+":add,"-":subtraction,"*":multiply,"/":divide}      

num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
for symbol in operations:
    print(symbol)
oper=input("Enter which operation you want to do ")
function=operations[oper]
result=function(num1,num2)
print(f"{num1}{oper}{num2}={result}")
progress=True
while progress==True:
    process=input("enter y if you want to perform operation or n for not")
    if process=="y":
        num3=int(input("Enter the number on which you want to perform next operation"))
        oper=input("Enter which operation you want to do ")
        function=operations[oper]
        result=function(result,num3)
        print(f"{result}{oper}{num3}={result}")
    else:
        print("You are done")
        progress=False






