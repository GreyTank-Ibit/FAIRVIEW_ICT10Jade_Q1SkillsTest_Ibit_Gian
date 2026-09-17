from pyscript import display, document

def confirm_info(e):
    document.getElementById("output1").innerHTML = ""
    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value
    display(f"Customer Name: {customer_name}", target="output1")
    display(f"Requested Items: {requested_items}", target="output1")

def create_order(e):
    document.getElementById("output2").innerHTML = ""
    total = 0

    if document.getElementById("item1").checked:
        qty = int(document.getElementById("qty1").value)
        total += 120 * qty
        display(f"{qty}x Classic Cheeseburger = Php{120 * qty}", target="output2")

    if document.getElementById("item2").checked:
        qty = int(document.getElementById("qty2").value)
        total += 150 * qty
        display(f"{qty}x Double Patty Cheeseburger = Php{150 * qty}", target="output2")

    if document.getElementById("item3").checked:
        qty = int(document.getElementById("qty3").value)
        total += 165 * qty
        display(f"{qty}x Large Cheeseburger = Php{165 * qty}", target="output2")

    if document.getElementById("item4").checked:
        qty = int(document.getElementById("qty4").value)
        total += 30 * qty
        display(f"{qty}x Fries = Php{30 * qty}", target="output2")

    if document.getElementById("item5").checked:
        qty = int(document.getElementById("qty5").value)
        total += 35 * qty
        display(f"{qty}x Cheesy Fries = Php{35 * qty}", target="output2")

    if document.getElementById("upsize").checked:
        total += 30
        display("Extra Cheese = Php30", target="output2")

    if document.getElementById("extra_ketchup").checked:
        total += 30
        display("Extra Ketchup = Php30", target="output2")

    if document.getElementById("w/o_Veggies").checked:
        total -= 30
        display("Without Veggies = -Php30", target="output2")

    display(f"Total: Php{total}", target="output2")

def show_order(e):
    document.getElementById("output3").innerHTML = ""
    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value
    display(f"Order Details: Customer Name: {customer_name}, Requested Items: {requested_items}", target="output3")