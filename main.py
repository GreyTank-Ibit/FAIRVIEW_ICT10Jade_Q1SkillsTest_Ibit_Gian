from pyscript import display
from js import document

grandtotal = 0
coffee_price = 0

def add_num(e): #Put e for the event handler
    document.getElementById("output1").innerHTML = " " #clears previous result

    num1 = float(document.getElementById("input1").value) #get input values
    num2 = float(document.getElementById("input2").value)
    result = num1 + num2 #use operator
    display(result, target="output1") #display result

def create_order(e):
    global grandtotal
    output = document.getElementById("output2")

    output.innerHTML = " " #clears previous result

    prod1 = document.getElementById("item1") #get item 1 element

    #calculate
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector("input[name='size']:checked")

    price = float(size.value)
    grandtotal = subtotal + price
    display(grandtotal, target="output2") #display result 

def place_order(e):
    global coffee_price
    output = document.getElementById("output3")
    output.innerHTML = " " #clears previous result 

    coffee = document.getElementById("coffee") #get coffee element
    coffee_price = float(coffee.value) 
    display(coffee_price, target="output3") #display result

def show_order(e):
    output = document.getElementById("output4")
    output.innerHTML = " " #clears previous result
    finalorder = grandtotal + coffee_price
    display(f'You have to pay a total of {finalorder}', target="output4") #display result