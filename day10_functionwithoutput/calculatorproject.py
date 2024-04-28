#Konsep Rekursi and Loop

from logocalculator import logo

#Add
def add(n1,n2):
    return n1 + n2
#Substract
def subs(n1,n2):
    return n1 - n2
#Multiply
def multi(n1,n2):
    return n1 * n2
#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subs,
    "*": multi,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))


    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2) #nama fungsinya dibuat variabel, jd kerja sesuai permintaan
    
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator() #ini rekursi, dia balik lagi ke atas, artinya dia bakal jadi True lagi

calculator()







