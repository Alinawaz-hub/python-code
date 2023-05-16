#calculater
#making the function for calculater

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divid(n1 , n2):
    return  n1 / n2

#making dictionary for symbols in calculater

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divid
}


def calculater():

#taking inputs 
    n1 = int(input("Enter the first number : "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("pick the symbol from given operations :  ")
        n2 = int(input("Enter the scend number : "))
        operations_function = operations[operation_symbol]
        answer = operations_function(n1 , n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")


#for taking second calculation with previous result
        if input(f"type 'y' to  continue with {answer} or type 'n' to start a new calculation : ") == "y":
            n1 = answer
        else:
            should_continue = False
            calculater()

calculater()   
     